import streamlit as st
from chatbot import chat_with_groq

st.set_page_config(page_title="💬 Groq Chatbot", layout="wide")

st.title("💬 Chat with Groq LLaMA 3 (70B)")
st.markdown("Fastest chatbot powered by **Groq LLaMA 3-70B**.")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        response = chat_with_groq(st.session_state.messages)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
