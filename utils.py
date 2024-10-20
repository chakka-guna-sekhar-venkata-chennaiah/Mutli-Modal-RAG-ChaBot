from openai import OpenAI
from langchain.vectorstores import FAISS
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.embeddings.base import Embeddings
from langchain.llms.base import LLM
from pydantic import BaseModel, Field
import streamlit as st
from sentence_transformers import SentenceTransformer

# Initialize the OpenAI client
client = OpenAI(
    api_key="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",  # Replace with your actual API key
    base_url="https://api.groq.com/openai/v1"
)

# Cache the model loading
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

# Load the model
model = load_model()

# Define custom embedding function
def custom_embedding_function(texts):
    return model.encode(texts)

# Create a custom Embeddings class
class CustomEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return custom_embedding_function(texts)
    
    def embed_query(self, text):
        return custom_embedding_function([text])[0]

# Instantiate the embeddings
embeddings = CustomEmbeddings()

# Load the FAISS indexes with custom embeddings
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