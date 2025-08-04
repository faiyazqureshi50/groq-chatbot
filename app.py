import streamlit as st
import time
from chatbot import chat_with_groq

st.set_page_config(page_title="💬 Groq Chatbot", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f9fafb;
        }

        .stChatMessage {
            word-wrap: break-word;
        }

        .message-container {
            background-color: #f1f2f6;
            border-radius: 12px;
            padding: 12px 16px;
            margin: 10px 0;
            line-height: 1.6;
            font-size: 16px;
        }

        .user {
            background-color: #cfe9ff;
            text-align: right;
        }

        .assistant {
            background-color: #e8f5e9;
        }

        @media only screen and (max-width: 600px) {
            .message-container {
                font-size: 17px;
            }
        }

        /* Chat bubble alignment */
        .st-emotion-cache-1c7y2kd {
            flex-direction: column-reverse;
        }
    </style>
""", unsafe_allow_html=True)

# Title & caption
st.title("🤖 Groq Chatbot")
st.caption("Powered by **LLaMA 3-70B via Groq** — Blazing fast and conversational.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(
            f"<div class='message-container {msg['role']}'>{msg['content']}</div>",
            unsafe_allow_html=True,
        )

# Chat input
if user_input := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(f"<div class='message-container user'>{user_input}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        response_text = chat_with_groq(st.session_state.messages)
        for char in response_text:
            full_response += char
            placeholder.markdown(f"<div class='message-container assistant'>{full_response}</div>", unsafe_allow_html=True)
            time.sleep(0.015)  # Typing animation speed
        st.session_state.messages.append({"role": "assistant", "content": full_response})
