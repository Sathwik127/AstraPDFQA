# 📄 AstraPDFQA

**AstraPDFQA** is an intelligent PDF Question Answering system built with LangChain, **Astra DB** (a serverless vector database by Datastax), HuggingFace Embeddings, and Google's Gemini LLM. It enables users to upload PDF files and ask questions directly from the content. Under the hood, the app uses **Astra DB's scalable vector store** to store semantic embeddings of PDF chunks and perform similarity search. This enables accurate and context-aware answers using retrieval-augmented generation (RAG). The Streamlit frontend provides a simple and intuitive user interface

---

## 🚀 Features

- 📤 Upload any PDF document
- 🤖 Ask questions about its content
- 🔍 Semantic search using vector embeddings
- 🧠 Contextual answers via Google's Gemini LLM
- ☁️ Astra DB as the vector store for scalable retrieval

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **LLM**: Gemini 1.5 Flash (`ChatGoogleGenerativeAI`)  
- **Vector Store**: Astra DB  
- **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)  
- **RAG Framework**: LangChain  
- **Document Loader**: LangChain PyPDFLoader  
- **Environment Management**: `dotenv`  

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AstraPDFQA.git
cd AstraPDFQA
```

### 2. Create a virtual environment

```bash
python -m venv env
```

Activate the virtual environment:

- **On macOS/Linux**:
  ```bash
  source env/bin/activate
  ```

- **On Windows**:
  ```bash
  env\Scripts\activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and add:

```env
ASTRA_DB_APPLICATION_TOKEN=your_astra_db_application_token
ASTRA_DB_API_ENDPOINT=your_astra_db_endpoint
GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```
Streamlit will start a local server and automatically open the frontend in your default web browser (like Chrome).
You'll see a message like this in your terminal:
for eg:
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501

---

## 📁 Project Structure

```
AstraPDFQA/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── README.md               # Project documentation
└── temp_uploaded.pdf       # Temporary uploaded file
```

---

## 📸 Screenshots:
to run code
<img width="845" height="277" alt="image" src="https://github.com/user-attachments/assets/92fa6f3d-70a8-43ef-9717-5084a66f7890" />
You can see this view your Streamlit app in your browser.
<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/a140f93e-0b3c-44e8-8486-9bc65a18acb7" />
you need to upload a file there 
<img width="1450" height="825" alt="image" src="https://github.com/user-attachments/assets/6431fb27-b755-4310-b52b-62ad1c41f9b4" />
you can ask questions about the pdf
<img width="1212" height="745" alt="image" src="https://github.com/user-attachments/assets/d5620e75-619a-46e3-9259-fca15fe66502" />
you can see the answers there 









---

## 🙌 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Google Gemini](https://ai.google.dev/)
- [Astra DB by Datastax](https://www.datastax.com/astra)
- [Streamlit](https://streamlit.io/)





