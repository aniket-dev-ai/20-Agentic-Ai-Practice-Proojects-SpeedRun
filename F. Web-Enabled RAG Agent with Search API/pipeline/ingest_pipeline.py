from Ingestion.chunker import chunker
from Ingestion.cleaner import cleaner
from Ingestion.search_tool import search_tool

from embeddings.embedding_model import embedding
from vectorstore.chroma_store import check_vector_store

from llm.gemini import model
from llm.embedding_model import embeddings_model

def ingest_pipeline(query): 
    content = search_tool(query) 
    document = cleaner(content)
    chunked_doc = chunker(document)
    vector_store = check_vector_store(embeddings_model)
    if embedding(chunked_doc , vector_store):
        return True
    else:
        return False
