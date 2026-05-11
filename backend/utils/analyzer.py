from langchain_community.llms import Ollama

llm = Ollama(model="phi")   # IMPORTANT (phi use karna)

def analyze_text(text):
    response = llm.invoke(text)
    return response