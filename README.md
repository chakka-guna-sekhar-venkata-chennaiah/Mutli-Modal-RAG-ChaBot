<h1 align='center'>🤖 MULTI-MODAL RAG APPLICATION 🤖</h1>
<h3 align='center'>Building Essence Toward's Personalized Knowledge Model (PKM)</h3>
<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/6f2bc880-fd32-41e1-b3b6-913e1592ff0a" alt="Flowcharts (0)">
</p>



# 1. Introduction
🌟 **Welcome to the Personal Knowledge Model (PKM) Project!** 🌟

🔍 **Discover the Future of Personalized Knowledge!**  
Our project draws inspiration from Microsoft's recent Recall initiative but takes a unique, user-centric approach. PKM uses advanced, on-device knowledge graph creation and updates, tailored weekly or monthly based on your interests. This ensures you can retrieve anything from your browsing history, search items, and mobile interactions, all at your fingertips!

🛡️ **Privacy First!**  
Unlike Microsoft Recall, which may expose user data through LLM inference, our approach guarantees your privacy with on-device knowledge graph operations. Your data never leaves your device, ensuring a fortress of privacy around your personal information.

🔧 **What We're Building:**  
Our repository is dedicated to crafting a multi-modal RAG (Retrieval-Augmented Generation) using PDFs and YouTube videos. Think of this project as your gateway to creating a Personal Knowledge Model (PKM). While still in development, our PKM leverages your device's GPU to generate sophisticated knowledge graphs on the fly.

🚀 **Current Focus:**  
For now, our eyes are set on multi-modal RAG applications using static data sources like PDFs and YouTube videos. The exciting part? Our RAG can retrieve relevant text, images, and video frames directly related to your queries!

👀 **Future Vision:**  
Microsoft recently unveiled GraphRAG, which currently supports CSV and TXT formats. We're aligning with this technology but expanding its capabilities to embrace PDF and video data, making our tool incredibly versatile.

🌐 **Open Source Collaboration:**  
This repository is open for contributions! We're inviting developers and enthusiasts to join us in achieving the PKM vision. Whether you're interested in pushing the boundaries of machine learning or just passionate about privacy-centric technology, your input is invaluable.

💻 **Static Multi-Modal RAG Application:**  
Imagine interacting with a system that understands and retrieves information across multiple media types without needing the computational powerhouses typically required for dynamic data processing. That's what we're aiming for—practical, accessible, and groundbreaking.

---

# 2. Basic Architectures for PKM, MMR-PDF (Multi-Modal RAG for PDF) & MMR-Video (Multi-Modal RAG for Video)
*  <h2>Basic PKM Architecture</h2>
<p align="center">
  <img src="https://github.com/chakka-guna-sekhar-venkata-chennaiah/Mutli-Modal-RAG-ChaBot/assets/110555361/1cb2a4aa-1a11-4b6d-875b-d9676c98edc8" alt="Flowcharts (1)">
</p>
  
* <h2>MMR-PDF (Multi-Modal RAG for PDF) Architecture (Static)</h2>
<p align="center">
  <img src="https://github.com/chakka-guna-sekhar-venkata-chennaiah/Mutli-Modal-RAG-ChaBot/assets/110555361/8e0788c4-8b87-4221-9d5a-9707ccccfce4" alt="Flowcharts (2)">
</p>

* <h2>MMR-Video (Multi-Modal RAG for Video) Architecture (Static)</h2>
<p align="center">
  <img src="https://github.com/chakka-guna-sekhar-venkata-chennaiah/Mutli-Modal-RAG-ChaBot/assets/110555361/ce045df8-f3c5-4d26-adc4-8fdb2540aa1f" alt="Flowcharts (3)">
</p>

# 3. Tech Stack
* 🧠 MindsDB OpenAI Endpoint [mdb.ai](https://mdb.ai/models)
* 🧩 Langchain
* 🖥️ Streamlit 
* 🗂️ FAISS

Here are the code block images for creating custom LLMs and embedding functions using LangChain's chain base class and MDB.ai endpoints. This is one of the trickiest parts of the project.

* Custom LLM function Code:-
<img width="1470" alt="Screenshot 2024-07-09 at 8 00 06 PM" src="https://github.com/chakka-guna-sekhar-venkata-chennaiah/Mutli-Modal-RAG-ChaBot/assets/110555361/4ad3d2e8-0c5b-481a-9107-5a1ab2a110dc">

* Custom Embedding function Code:-
<img width="1470" alt="Screenshot 2024-07-09 at 7 59 24 PM 1" src="https://github.com/chakka-guna-sekhar-venkata-chennaiah/Mutli-Modal-RAG-ChaBot/assets/110555361/c3f06cd7-2a5e-4cac-90ea-bc5908423bc4">




# 4. Steps to Run the Project

### Step 1: Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/chakka-guna-sekhar-venkata-chennaiah/Mutli-Modal-RAG-ChaBot.git
```


### Step 2: Navigate to the Repository
Change into the repository directory:
```bash
cd Mutli-Modal-RAG-ChaBot
```

### Step 3: Install Required Libraries
Install all the necessary libraries:
```bash
python -m pip install -r requirements.txt
```

### Step 4: Create the Secrets File
Before running the Streamlit application, create a folder named `.streamlit`. Inside this folder, create a file named `secrets.toml` and add the following code:
```toml
api_key='your-minds-api-key'
```

### Step 5: Initialize the User Interface
Launch the Streamlit application:
```bash
python -m streamlit run app.py
```

### Important Note:
As mentioned earlier, this repository is built using the [Monuments of National Importance PDF](https://eacpm.gov.in/wp-content/uploads/2023/01/Monuments-of-National-Importance.pdf) and a [YouTube video](https://www.youtube.com/watch?v=rRZdtAGInyQ&list=PLhRXULtLjLtfQ9COvoZg8Zg6ejTI3UPTG&index=1). If you wish to use your own resources, please follow the steps in the available Colab notebooks and replace the FAISS index files accordingly. Feel free to customize `app.py` to suit your needs.

Our ultimate goal is to develop a Personalized Knowledge Model (PKM) and a dynamic multi-modal RAG system. This repository serves as a gateway to achieving that vision, and we welcome your support and contributions to help make it a reality.

# 4. Demo (Detailed Explanation)
<p align="center">
    <a href="https://www.youtube.com/watch?v=eIqJR4UWiFM">
      <img src="https://github.com/chakka-guna-sekhar-venkata-chennaiah/Mutli-Modal-RAG-ChaBot/assets/110555361/4471e1c3-91c7-478b-8dbd-bd48043ffd87" style="width: 300px; height: 300px; object-fit: cover;">
    </a>
</p>

For Quick Demo, Watch 👀 


[Quick Demo](https://github.com/chakka-guna-sekhar-venkata-chennaiah/Mutli-Modal-RAG-ChaBot/assets/110555361/60ff76f6-b9f5-42e8-87e9-fc5a66e6dc34)

[Live WebApp Prototype](https://mutli-modal-rag-chabot.streamlit.app/)


# 5. Future Enhancements
- [ ] Dynamic Multi-Modal RAG Application
- [ ] Integration with Real-Time on device data for creating advanced knoweldge graphs

### ⭐ If you find this repository useful, please star it! ⭐

### Meet the Author

**GitHub:** [chakka-guna-sekhar-venkata-chennaiah](https://github.com/chakka-guna-sekhar-venkata-chennaiah)

**LinkedIn:** [Chakka Guna Sekhar Venkata Chennaiah](https://www.linkedin.com/in/chakka-guna-sekhar-venkata-chennaiah-7a6985208/)

**X (formerly Twitter):** [@codevlogger](https://x.com/codevlogger)

Thank you for being a part of our journey to create an advanced, personalized knowledge system! 🌟
