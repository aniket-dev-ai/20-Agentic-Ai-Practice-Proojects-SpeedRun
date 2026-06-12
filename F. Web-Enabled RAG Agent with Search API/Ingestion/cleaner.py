from langchain_core.documents import Document

def cleaner(content):
    print("Cleaning search results and preparing documents...")
    document = [
        Document(
            page_content=c['raw_content'],
            metadata={"title": c['title'], "url": c['url']}) for c in content['results']]
    
    print("Search results cleaned and documents prepared successfully.")
    return document