import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

dimension = 384 
index = faiss.IndexFlatL2(dimension)

def store_embedding(text, index):
    embedding = model.encode([text])
    index.add(np.array(embedding, dtype=np.float32))

def search_in_faiss(query, index, data, k=1):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding, dtype=np.float32), k)
    if I[0][0] != -1:
        return data[I[0][0]]
    else:
        return "Desculpe, não encontrei uma resposta relevante."

car_info = [
    "O Marea é o melhor carro feito no Brasil.",
    "O motor 20V do Marea é o mais potente do Brasil.",
    "A manutenção do carro deve incluir troca de óleo a cada 5000 km.",
    "Carros esportivos geralmente têm uma suspensão mais rígida para melhorar a estabilidade.",
    "A pressão dos pneus deve ser verificada regularmente para garantir segurança e economia de combustível.",
    "O Toyota Corolla é conhecido por sua confiabilidade e durabilidade ao longo dos anos.",
    "Carros com transmissão automática costumam ser mais confortáveis para dirigir em trânsito pesado.",
    "O motor turbo oferece mais potência e torque, mas pode consumir mais combustível.",
    "SUVs são carros populares para famílias devido ao espaço interno e à altura elevada.",
    "O sistema de freios ABS ajuda a evitar que as rodas travem durante uma frenagem brusca.",
    "A calibragem dos pneus deve ser feita a cada duas semanas para garantir um bom desempenho.",
    "Carros elétricos têm menor custo de manutenção, pois possuem menos partes móveis.",
    "Um carro híbrido combina um motor a combustão com um motor elétrico para maior eficiência.",
    "O sistema de direção elétrica é mais leve e econômico do que o sistema hidráulico.",
    "A troca do filtro de ar ajuda a manter o motor funcionando de maneira eficiente.",
    "O motor a diesel é mais econômico para longas distâncias e oferece mais torque.",
    "A troca de pastilhas de freio deve ser feita ao notar desgaste ou perda de eficiência.",
    "O Volkswagen Golf GTI é um dos hatchbacks esportivos mais populares no mundo.",
    "Carros com tração nas quatro rodas oferecem melhor aderência em terrenos difíceis.",
    "Veículos com teto solar permitem mais luz natural e ventilação no interior do carro.",
    "O uso do ar-condicionado em dias quentes pode aumentar o consumo de combustível.",
    "Motores de seis cilindros são conhecidos por oferecerem um equilíbrio entre potência e economia.",
    "A revisão do carro deve incluir a inspeção dos freios, filtros, óleo e sistema de arrefecimento.",
    "Faróis de LED consomem menos energia e oferecem melhor visibilidade do que faróis halógenos.",
    "Carros conversíveis oferecem uma experiência única, mas podem ter maior consumo de combustível.",
]

for info in car_info:
    store_embedding(info, index)

st.title("Chatbot sobre Carros")
st.write("Digite uma pergunta sobre carros.")

user_message = st.text_input("Sua mensagem:")

if st.button("Enviar"):
    bot_response = search_in_faiss(user_message, index, car_info)
    st.write(f"Bot: {bot_response}")
