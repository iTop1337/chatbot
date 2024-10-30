from weaviate import Client
from langchain_community.vectorstores import Weaviate

def initialize_vector_store():
    client = Client("http://localhost:8080")

    index_name = "Document" 
    text_key = "content"     

    vector_store = Weaviate(client, index_name=index_name, text_key=text_key)
    return vector_store
