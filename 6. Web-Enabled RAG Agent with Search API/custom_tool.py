from langchain.tools import tool
from pipeline.ingest_pipeline import ingest_pipeline
from pipeline.retrieval_pipeline import retrieval_pipeline

@tool
def ingest_tool(query: str):
    """Search web news and store into vector database."""
    return ingest_pipeline(query)


@tool
def retrieve_tool(query: str):
    """Retrieve relevant chunks from vector database."""
    return retrieval_pipeline(query)

tools = [ingest_tool , retrieve_tool]