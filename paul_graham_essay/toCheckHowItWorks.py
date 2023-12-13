from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)
while True:
    
    quetion=input("enter your quetion here:")
    query_engine = index.as_query_engine()
    response = query_engine.query(quetion)
    print(response)