from langchain_community.document_loaders import CSVLoader
from langchain_core.tools import tool

@tool
def load_csv_data(file_path: str) -> str:
    """Loads content from a CSV file and returns it as a string."""
    loader = CSVLoader(file_path=file_path)
    # Load the documents
    documents = loader.load()
    
    # Combine document content into a single string for the tool response
    return "\n\n".join([doc.page_content for doc in documents])

# Usage
# result = load_csv_data.invoke({"file_path": "data.csv"})