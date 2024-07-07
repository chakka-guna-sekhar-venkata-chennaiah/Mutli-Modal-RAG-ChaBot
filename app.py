import base64
import streamlit as st
import time
from utils import answer


st.set_page_config(layout="wide",initial_sidebar_state="expanded",
                   page_icon='🤖',page_title='Mutli-Modal RAG WebApp')



page = st.sidebar.selectbox("Jump to... 👇", ["About", "Demo"])

with st.sidebar:
    st.image('techs.png')
    style = """
            <style>
                .author-section {
                    text-align: center;
                    margin-top: 20px;
                    font-family: Arial, sans-serif;
                }
                .author-section h3 {
                    color: #0a9396;
                    margin-bottom: 10px;
                }
                .author-links a {
                    color: #005f73;
                    text-decoration: none;
                    font-size: 18px;
                    font-weight: bold;
                    display: block;
                    margin: 5px 0;
                    background: #e0fbfc;
                    border-radius: 5px;
                    padding: 8px 20px;
                    transition: all 0.3s ease;
                }
                .author-links a:hover {
                    background: #94d2bd;
                    color: #fff;
                    transform: translateY(-2px);
                }
            </style>
            """

            # Embed the HTML with custom styles in Streamlit's markdown renderer
    st.markdown(style, unsafe_allow_html=True)
    st.markdown(
                '''
                <div class="author-section">
                    <h3>🌟 Meet the Author</h3>
                    <div class="author-links">
                        <a href="https://www.linkedin.com/in/chakka-guna-sekhar-venkata-chennaiah/" target="_blank">LinkedIn</a>
                        <a href="https://twitter.com/codevlogger" target="_blank">X</a>
                        <a href="https://github.com/chakka-guna-sekhar-venkata-chennaiah" target="_blank">GitHub</a>
                    </div>
                </div>
                ''',
                unsafe_allow_html=True
            )
    st.warning("Heads up, lovely users!** 🌟 Our clever bot uses RAG with LLMs which, while usually spot on, can sometimes dream up its own little facts. Just a cute reminder to double-check those extra imaginative responses! 💫")


if page=='About':
   # Define custom style for the glowing text
    glowing_text_style = '''
    <style>
        .glowing-text {
            font-family: 'Arial Black', sans-serif;
            font-size: 45px;
            text-align: center;
            color: #FFFFFF;
            background: linear-gradient(270deg, #ff9d76, #ff6263, #ff2a6d, #e959d9, #53a2ff, #23f0c7);
            background-size: 300% 300%;
            animation: GradientShift 15s ease infinite;
        }
        
        @keyframes GradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
    </style>
'''

    # Display the glowing text using st.markdown
    st.markdown(glowing_text_style, unsafe_allow_html=True)
    st.markdown(f'<p class="glowing-text"> 🤖 Multi-Modal RAG WebApp 🤖</p>', unsafe_allow_html=True)
    st.image('multimodal.png')
    st.success("🚀 Explore the [Google Colab Notebook](https://colab.research.google.com/drive/18DK5oD1CA1prweSd0cOOopcAs7oM2eGY?usp=sharing) for an exciting journey through multimodal vector databases, creating custom LLMs with MindsDB endpoints, and much more! 🧠💡")

else:
    glowing_text_style = '''
    <style>
        .glowing-text {
            font-family: 'Arial Black', sans-serif;
            font-size: 45px;
            text-align: center;
            color: #FFFFFF;
            transition: transform 0.1s;
            perspective: 500px;
            animation: rotateText 10s linear infinite;
        }

        @keyframes rotateText {
            0% { transform: rotateY(0deg) rotateX(0deg); }
            25% { transform: rotateY(15deg) rotateX(15deg); }
            50% { transform: rotateY(-15deg) rotateX(-15deg); }
            75% { transform: rotateY(15deg) rotateX(-15deg); }
            100% { transform: rotateY(-15deg) rotateX(15deg); }
        }
    </style>
'''
        # Display the glowing text using st.markdown
    st.markdown(glowing_text_style, unsafe_allow_html=True)
    st.markdown(f'<p class="glowing-text"> 🤖 Multi-Modal RAG ChatBot 🤖</p>', unsafe_allow_html=True)
    user_input = st.text_area(label="You can ask me anything from the [PDF](https://eacpm.gov.in/wp-content/uploads/2023/01/Monuments-of-National-Importance.pdf)")
    if st.button("Submit"):
        
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get the answer
        result, relevant_images = answer(user_input)

        # Show the answer
        with st.chat_message("assistant"):
        
            with st.spinner('🖊️ 🖊️ 🖊️...'):
                time.sleep(2)

        st.markdown(result)

        if len(relevant_images)>0:
            # Display a success message
            st.success('Relevant Image Found....')
            with st.spinner('📷 📷 📷...'):
                time.sleep(2)
            img_bytes = base64.b64decode(relevant_images[0])
            st.image(img_bytes)

        
