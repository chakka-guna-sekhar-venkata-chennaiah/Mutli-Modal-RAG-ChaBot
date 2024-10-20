import base64
import streamlit as st
import time
from utils import answer, answer1




page = st.sidebar.selectbox("Jump to... 👇", ["About", "Demo","MMR-PDF",'MMR-Video'])


if page=='About':
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
    st.success("📣 I highly suggest 💡 you check out the 'demo' subpage 🌐 for a more comprehensive understanding 🧠 of the app and how to use it 📱. It's really helpful! 👍")
    

elif page=='Demo':
    st.markdown("""
                <h1 align='center'>
                📹 Check out the demo video below 👇</h1>
                """,unsafe_allow_html=True)
    st.video("demo/demo.mp4")
elif page=='MMR-PDF':
    with st.sidebar:
        st.write("[Monuments-of-National-Importance PDF](https://eacpm.gov.in/wp-content/uploads/2023/01/Monuments-of-National-Importance.pdf)")
        st.markdown('----')
        st.markdown('<p style="text-align: center;">Wanna create your own Multi-Modal RAG using your PDF resource</a>? 📚🎨</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center;">Dive into our detailed <a href="https://colab.research.google.com/drive/1m4pSzPAtWzJlgmxZIbgZ5I5jwtfACYUW?usp=sharing" target="_blank" style="background-color: #ffffff; color: #000000; padding: 2px 5px; border-radius: 3px; text-decoration: none;">Google Colab Notebook</a> and make your project truly unique! ✨🚀</p>', unsafe_allow_html=True)

        
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
    st.markdown(f'<p class="glowing-text"> 🤖 Multi-Modal RAG ChatBot (PDF) 🤖</p>', unsafe_allow_html=True)
    st.warning("Disclaimer: This project is built based on the attached PDF in the sidebar 👈 . If you wish to replicate it, please follow the tutorial links provided in the sidebar using your own resources.")
    user_input = st.text_area(label="Please feel free to ask me any questions related to the content of the PDF linked on the sidebar to your left 👈.")

    if st.button("Submit"):
        
        col1,col2=st.columns(2)

        with col1:
            st.success('Normal RAG')
            with st.chat_message("user"):
                st.markdown(user_input)

            # Get the answer
            result, relevant_images = answer(user_input)

            # Show the answer
            with st.chat_message("assistant"):
            
                with st.spinner('🖊️ 🖊️ 🖊️...'):
                    time.sleep(2)

            st.markdown(result)

            
        with col2:
            st.success('Multi Modal RAG')
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
                st.success('Relevant Frame Found....')
                with st.spinner('📷 📷 📷...'):
                    time.sleep(2)
                img_bytes = base64.b64decode(relevant_images[0])
                st.image(img_bytes)

else:
    with st.sidebar:
        st.video("https://www.youtube.com/watch?v=rRZdtAGInyQ&list=PLhRXULtLjLtfQ9COvoZg8Zg6ejTI3UPTG&index=1")
        st.markdown('---')
        st.markdown('<p style="text-align: center;">Wanna create your own Multi-Modal RAG using your Video resource</a>? 📚🎨</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center;">Dive into our detailed <a href="https://colab.research.google.com/drive/18DK5oD1CA1prweSd0cOOopcAs7oM2eGY?usp=sharing" target="_blank" style="background-color: #ffffff; color: #000000; padding: 2px 5px; border-radius: 3px; text-decoration: none;">Google Colab Notebook</a> and make your project truly unique! ✨🚀</p>', unsafe_allow_html=True)

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
    st.markdown(f'<p class="glowing-text"> 🤖 Multi-Modal RAG ChatBot (Video) 🤖</p>', unsafe_allow_html=True)
    st.warning("Disclaimer: This project is built based on the attached Video in the sidebar 👈 . If you wish to replicate it, please follow the tutorial links provided in the sidebar using your own resources.")
    user_input = st.text_area(label="Feel free to inquire about any information or topic present in the Video that is conveniently displayed on the sidebar to your left 👈.")
    if st.button("Submit"):
        
        col1,col2=st.columns(2)

        with col1:
            st.success('Normal RAG')
            with st.chat_message("user"):
                st.markdown(user_input)

            # Get the answer
            result, relevant_images = answer1(user_input)

            # Show the answer
            with st.chat_message("assistant"):
            
                with st.spinner('🖊️ 🖊️ 🖊️...'):
                    time.sleep(2)

            st.markdown(result)

            
        with col2:
            st.success('Multi Modal RAG')
            with st.chat_message("user"):
                st.markdown(user_input)

            # Get the answer
            result, relevant_images = answer1(user_input)

            # Show the answer
            with st.chat_message("assistant"):
            
                with st.spinner('🖊️ 🖊️ 🖊️...'):
                    time.sleep(2)

            st.markdown(result)

            if len(relevant_images)>0:
                # Display a success message
                st.success('Relevant Frame Found....')
                with st.spinner('📷 📷 📷...'):
                    time.sleep(2)
                img_bytes = base64.b64decode(relevant_images[0])
                st.image(img_bytes)



        
