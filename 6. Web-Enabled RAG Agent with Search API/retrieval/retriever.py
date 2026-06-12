from langchain_classic.retrievers.multi_query import MultiQueryRetriever

def retriever(vector_store , model ,query):
    base_retriever = vector_store.as_retriever(
    search_kwargs={"k": 15}
    )
    
    retriever = MultiQueryRetriever.from_llm(
        retriever=base_retriever,
        llm=model
    )
    
    print("Invoking retriever with query:", query)
    docs = retriever.invoke(query)
    print(f"Retrieved {len(docs)} documents.")
    
    return docs