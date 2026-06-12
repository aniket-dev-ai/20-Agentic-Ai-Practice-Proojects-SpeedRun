from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool


api_wrapper = WikipediaAPIWrapper(top_k_results=3, lang="en", doc_content_chars_max=500 , wiki_client=None)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

