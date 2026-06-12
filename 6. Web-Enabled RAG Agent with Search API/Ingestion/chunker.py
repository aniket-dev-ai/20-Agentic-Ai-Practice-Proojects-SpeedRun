from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter( 
    chunk_size=1000,
    chunk_overlap=150, 
)

def chunker(document):
    print("Splitting document into chunks...")
    doc = text_splitter.split_documents(document)    
    print("Document split into chunks successfully.")
    return doc