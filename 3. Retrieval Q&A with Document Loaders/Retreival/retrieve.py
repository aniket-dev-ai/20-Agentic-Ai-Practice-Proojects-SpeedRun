from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from langchain.tools import tool
from embeddings.embedding import vector_store , embeddings

@tool
def retrieve(query: str):
    """Perform a similarity vector search for the given query."""
    results = vector_store.similarity_search_by_vector(
        embedding=embeddings.embed_query(query), k=1
    )
    return [f"* {doc.page_content} [{doc.metadata}]" for doc in results]