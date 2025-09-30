import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")