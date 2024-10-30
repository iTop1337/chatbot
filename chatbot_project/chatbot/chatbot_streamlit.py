import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_llm_response(message):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=message,
        max_tokens=50,
    )
    return response.choices[0].text.strip()

st.title("Chatbot com LLM")
st.write("Digite uma mensagem para conversar com o chatbot.")

user_message = st.text_input("Sua mensagem:")

if st.button("Enviar"):
    bot_response = get_llm_response(user_message)
    st.write(f"Bot: {bot_response}")
