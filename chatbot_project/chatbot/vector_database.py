from langchain import Weaviate 

def inialize_vector_store():
        vector_store = Weaviate(
                url="https://localhost:8080",
                auth_client_secret=None
        )

        return vector_store