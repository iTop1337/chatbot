from vector_database import initialize_vector_store

try:
    vector_store = initialize_vector_store()
    print("Conexão bem-sucedida com o Weaviate!")
except Exception as e:
    print(f"Erro ao conectar com o Weaviate: {e}")
