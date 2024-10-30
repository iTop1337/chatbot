import os 
from langchain.chains import ConversationalChain
from langchain.llms import Openai
from langgraph import LangGraph 


def setup_chabot():
    api_key = os.getenv("LLM_API_KEY")
    llm = Openai(api_key=api_key)

    graph = LangGraph()

    chain = ConversationalChain(llm=llm)
    return chain 