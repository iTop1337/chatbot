import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#FAISS
dimension = 384
index = faiss.IndexFlatL2(dimension)

#BASE
car_info = [
    "O Marea é o melhor carro feito no Brasil.",
    "O motor 20V do Marea é o mais potente do Brasil.",
    "A manutenção do carro deve incluir troca de óleo a cada 5000 km."
]
car_info_embeddings = []

def store_embedding(text):
    embedding = model.encode([text])
    index.add(np.array(embedding, dtype=np.float32))
    car_info_embeddings.append(text)

for info in car_info:
    store_embedding(info)

def search_in_faiss(query, threshold=0.5):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding, dtype=np.float32), k=1)
    if D[0][0] < threshold:
        return car_info_embeddings[I[0][0]]
    else:
        return "Desculpe, não encontrei uma resposta relevante."

st.title("Chatbot sobre Carros com FAISS")
st.write("Digite uma pergunta sobre carros.")

user_message = st.text_input("Sua mensagem:")

if st.button("Enviar"):
    bot_response = search_in_faiss(user_message)
    st.write(f"Bot: {bot_response}")
