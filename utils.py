from openai import OpenAI
from langchain.vectorstores import FAISS
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.embeddings.base import Embeddings
from langchain.llms.base import LLM
from pydantic import BaseModel, Field
import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer
import torch
from transformers import AutoTokenizer, AutoModel

# Initialize the OpenAI client
client = OpenAI(
    api_key=st.secrets['api_key'],  
    base_url="https://api.groq.com/openai/v1"
)



@st.cache_resource
def load_jina_model():
    tokenizer = AutoTokenizer.from_pretrained("jinaai/jina-embeddings-v2-base-en")
    model = AutoModel.from_pretrained("jinaai/jina-embeddings-v2-base-en")
    return tokenizer, model

tokenizer, model = load_jina_model()

def get_jina_embeddings(texts, model, tokenizer):
    # Tokenize the input texts
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
    
    # Generate embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Use the [CLS] token embeddings as sentence embeddings
    embeddings = outputs.last_hidden_state[:, 0, :].numpy()
    
    # Normalize the embeddings
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    
    return embeddings

def upscale_embedding(embedding, target_dim=1536):
    """Upscale embedding to target dimensions."""
    if len(embedding) >= target_dim:
        return embedding[:target_dim]  # Truncate if larger
    
    # Calculate scaling factor
    scale = target_dim / len(embedding)
    
    # Use linear interpolation to upscale
    upscaled = np.interp(
        np.linspace(0, len(embedding) - 1, target_dim),
        np.arange(len(embedding)),
        embedding
    )
    
    return upscaled

class JinaEmbeddings(Embeddings):
    def embed_documents(self, texts):
        embeddings = get_jina_embeddings(texts, model, tokenizer)
        return np.array([upscale_embedding(emb) for emb in embeddings])
    
    def embed_query(self, text):
        embedding = get_jina_embeddings([text], model, tokenizer)[0]
        return upscale_embedding(embedding)

embeddings = JinaEmbeddings()

@st.cache_resource
def load_faiss_indexes():
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    db1 = FAISS.load_local("faiss_index_audio", embeddings, allow_dangerous_deserialization=True)
    return db, db1

db, db1 = load_faiss_indexes()


# Define the prompt template
prompt_template = """
You are an assistant tasked with summarizing tables and text.
Give a concise summary of the table or text.
Answer the question based only on the following context, which can include text, images, and tables:
{context}
Question: {question}
Don't answer if you are not sure and decline to answer and say "Sorry, I don't have much information about it."
Just return the helpful answer in as much detail as possible.
Answer:
"""

def get_llm_output(context, question):
    formatted_prompt = prompt_template.format(context=context, question=question)
    
    completion = client.chat.completions.create(
        model="gemma-7b-it",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": formatted_prompt}
        ]
    )
    
    return completion.choices[0].message.content

# Define the answer function to handle queries
def answer(question):
    relevant_docs = db.similarity_search(question)
    context = ""
    relevant_images = []
    for d in relevant_docs:
        if d.metadata['type'] == 'text':
            context += '[text]' + d.metadata['original_content']
        elif d.metadata['type'] == 'table':
            context += '[table]' + d.metadata['original_content']
        elif d.metadata['type'] == 'image':
            context += '[image]' + d.page_content
            relevant_images.append(d.metadata['original_content'])
            
    result = get_llm_output(context, question)
    return result, relevant_images

# Query the vectorstore
def answer1(question):
    relevant_docs = db1.similarity_search(question)
    context = ""
    relevant_images = []
    for d in relevant_docs:
        if d.metadata['type'] == 'text':
            context += '[text]' + d.metadata['original_content']
        elif d.metadata['type'] == 'image':
            context += '[image]' + d.page_content
            relevant_images.append(d.metadata['original_content'])
    result = get_llm_output(context, question)
    return result, relevant_images



#code completed
