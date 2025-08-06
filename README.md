# 📄 AstraPDFQA

**AstraPDFQA** is an intelligent PDF Question Answering system built with LangChain, Astra DB, HuggingFace Embeddings, and Google's Gemini LLM. It enables users to upload PDF files and ask questions directly from the content. Under the hood, the app uses vector-based semantic search and retrieval-augmented generation (RAG) to deliver accurate and context-aware answers. The Streamlit frontend provides a simple and intuitive user interface.

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

Then open the URL shown in your terminal (usually http://localhost:8501).

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

## 📸 Screenshots

> Coming soon!

---

## 🙌 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Google Gemini](https://ai.google.dev/)
- [Astra DB by Datastax](https://www.datastax.com/astra)
- [Streamlit](https://streamlit.io/)

---

## 📝 License

This project is licensed under the MIT License.

---

## 💡 Future Improvements

- ✅ Multi-document support  
- ✅ Better error handling  
- ✅ Chat history / memory  
- ✅ PDF preview in UI  
- ✅ Authentication for user-based access  

---

## ✨ Made with ❤️ using AstraDB and AI

