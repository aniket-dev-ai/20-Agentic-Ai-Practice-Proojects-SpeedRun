from langchain_classic.retrievers.multi_query import MultiQueryRetriever

def retriever(vector_store, model, query):
    base_retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20,
        "lambda_mult": 0.7
    }
    )

    mq_retriever = MultiQueryRetriever.from_llm(
        retriever=base_retriever,
        llm=model
    )

    print("Invoking retriever with query:", query)
    docs = mq_retriever.invoke(query)
    print(f"Retrieved {len(docs)} documents before rerank.")

    return docs