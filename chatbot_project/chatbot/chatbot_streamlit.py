import streamlit as st
import requests

st.title("Chatbot")
st.write("Digite uma mensagem para conversar com o chatbot.")

user_message = st.text_input("Sua mensagem:")

if st.button("Enviar"):
    response = requests.post(
        "http://localhost:8000/api/chat/message/", 
        data={"message": user_message}
    )

    if response.status_code == 200:
        bot_response = response.json().get("response")
        st.write(f"Bot: {bot_response}")
    else:
        st.write("Erro ao se comunicar com o chatbot.")
