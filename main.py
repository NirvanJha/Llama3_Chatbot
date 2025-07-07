import streamlit as st
import requests

# --- CONFIG ---
MODEL_NAME = "gemma3:latest"  # ✅ Update to match the model listed via `ollama list`
OLLAMA_URL = "http://localhost:11434/api/generate"

# --- STREAMLIT PAGE SETUP ---
st.set_page_config(page_title="LLaMA Local Chatbot", page_icon="🦙", layout="centered")
st.title("🦙 LLaMA 3 Chatbot (Local + Free via Ollama)")

# --- CHAT HISTORY STATE ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- DISPLAY CHAT HISTORY ---
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- USER INPUT ---
user_input = st.chat_input("Ask your question...")

# --- FUNCTION TO CALL OLLAMA ---
def query_llama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"⚠️ Ollama Error: {response.text}"
    except requests.exceptions.ConnectionError:
        return "🚫 Ollama server not running. Please run: `ollama run llama3:8b`"

# --- HANDLE CHAT ---
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        reply = query_llama(user_input)

    st.session_state.chat_history.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)

# --- FOOTER ---
st.markdown("---")
st.caption("✨ Powered Locally by Ollama + LLaMA 3")
