from langchain_chroma import Chroma

def check_vector_store(embeddings):
    persist_directory = "web_search_db"
    
    try:
        print("Checking if vector store exists...")
        vector_store = Chroma(
            embedding_function=embeddings,
            persist_directory=persist_directory,
            collection_name="Search_Collection"
        )
        if vector_store._collection.count() > 0:
            print("Vector store already exists. Loading existing store.")
            return vector_store
    except:
        pass
    
    print("Creating vector store...")
    vector_store = Chroma(
            embedding_function=embeddings,
            persist_directory=persist_directory,
            collection_name="Search_Collection"
        )
    print("Vector store created successfully.")
    return vector_store