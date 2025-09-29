from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from .embeddings import get_embeddings
from .loaders import load_document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings


def build_qa_chain(file_path):
    # Load and split the document into chunks
    documents = load_document(file_path)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    docs = splitter.split_documents(documents)

    # Create embeddings and vector store
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Build RetrievalQA chain with the retriever
    return RetrievalQA.from_chain_type(
        llm=ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        ),
        retriever=vectorstore.as_retriever()
    )

