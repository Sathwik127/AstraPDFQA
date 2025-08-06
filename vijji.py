from astrapy import DataAPIClient
from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Initialize Astra DB Client
client = DataAPIClient(os.getenv("ASTRA_DB_APPLICATION_TOKEN"))
db = client.get_database_by_api_endpoint(
  os.getenv("ASTRA_DB_API_ENDPOINT")
)



# Initialize embedding model and vector store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vstore = AstraDBVectorStore(
    embedding=embeddings,
    collection_name="pdf_rag",
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT")
)

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key="AIzaSyBBfDhUQhlWNF3rpygQ3XLH9a1ReXtx8cE"
)

# Streamlit UI
st.set_page_config(page_title="PDF Q&A")
st.title("📄 PDF Question Answering App")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file to a temporary location
    temp_path = os.path.join("temp_uploaded.pdf")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Proceed with loading the PDF
    loader = PyPDFLoader(temp_path)
    pages = loader.load_and_split()
    collection = db["pdf_rag"]
    collection.delete_many({})
    # Add documents to AstraDB vector store
    vstore.add_documents(pages)

    # Build the retrieval QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vstore.as_retriever(),
        chain_type="stuff"
    )

    question = st.text_input("Ask a question from the uploaded PDF:")

    if st.button("Get Answer"):
        if question.strip():
            response = qa_chain.invoke(question)
            st.write("### 🤖 Answer:")
            st.write(response["result"])
        else:
            st.warning("Please enter a question.")
else:
    st.info("Upload a PDF file to begin.")
