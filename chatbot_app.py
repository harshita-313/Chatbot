# chatbot_app.py

import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="🤖 General Knowledge Chatbot")
st.title("🧠 Ask Me Anything - Local AI Chatbot")

@st.cache_resource
def load_model():
    return Ollama(model="mistral")

llm = load_model()

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    verbose=False
)

user_input = st.text_input("Ask me anything:", "")

if user_input:
    with st.spinner("🤔 Thinking..."):
        response = conversation.run(user_input)
        st.markdown("### 🤖 Answer:")
        st.write(response)
