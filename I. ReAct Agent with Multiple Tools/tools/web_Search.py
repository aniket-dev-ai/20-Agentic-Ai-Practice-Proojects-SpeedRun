from langchain.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

search_engine = TavilySearch(
    max_results=5,
    topic="general",
    search_depth="basic",
    time_range="week",
)

@tool
def search_tool(query: str) -> str:
    """
    Search the web for relevant information.
    """
    results = search_engine.invoke(query)
    return str(results)