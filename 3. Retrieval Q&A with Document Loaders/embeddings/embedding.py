from pathlib import Path
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b",
    dimensions=1024,
)

vector_store = Chroma(
    collection_name="gta6-documents",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db"
)
