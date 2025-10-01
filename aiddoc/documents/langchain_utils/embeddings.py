import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    
    # return HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    try:
        return GoogleGenerativeAIEmbeddings(
        model_name="gemini-pro",
        api_key=os.getenv("GOOGLE_API_KEY")
    )
    except Exception as e:
        print(f"Error initializing GoogleGenerativeAIEmbeddings: {e}")
        return HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")