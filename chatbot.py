import httpx
import streamlit as st  # ✅ Import streamlit to use st.secrets

# No need for dotenv in deployment
# from dotenv import load_dotenv
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]  # ✅ Use secrets directly

def chat_with_groq(messages, model="llama3-70b-8192"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7
    }

    try:
        response = httpx.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {e}"
