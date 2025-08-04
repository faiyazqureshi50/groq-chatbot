import streamlit as st
import time
from chatbot import chat_with_groq

st.set_page_config(page_title="💬 Groq Chatbot", layout="centered")

st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
        }
        .stChatMessage {
            max-width: 100%;
            word-wrap: break-word;
        }
        .message-container {
            background-color: #f1f2f6;
            border-radius: 15px;
            padding: 10px 15px;
            margin-bottom: 10px;
        }
        .assistant {
            background-color: #dff9fb;
        }
        .user {
            background-color: #c7ecee;
        }
        @media only screen and (max-width: 600px) {
            .message-container {
                font-size: 16px;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Groq Chatbot")
st.caption("Powered by **LLaMA 3-70B via Groq** — Blazing fast.")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Render previous chat messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(f"<div class='message-container {msg['role']}'>" + msg["content"] + "</div>", unsafe_allow_html=True)

# Input box
if user_input := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(f"<div class='message-container user'>{user_input}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        for word in chat_with_groq(st.session_state.messages).split():
            full_response += word + " "
            placeholder.markdown(f"<div class='message-container assistant'>{full_response}</div>", unsafe_allow_html=True)
            time.sleep(0.03)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
