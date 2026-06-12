from langchain_tavily import TavilySearch 

from dotenv import load_dotenv
load_dotenv()

tool = TavilySearch(
    max_results=5,
    topic="news",
    include_raw_content=True,
    search_depth="basic",
    time_range="week", 
    country="india",   
)

def search_tool(query):
    print("Searching for relevant information...")
    search_results = tool.invoke(query)
    print("Search completed successfully.")
    return search_results