from llm.gemini import model
from llm.embedding_model import embeddings_model
from retrieval.retriever import retriever
from vectorstore.chroma_store import check_vector_store

def retrieval_pipeline(query):
    vector_store = check_vector_store(embeddings_model)
    retreived_chunks = retriever(vector_store , model , query)
    return retreived_chunks