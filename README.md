# Llama3_Chatbot
# 🦙 LLaMA 3 Local Chatbot with Streamlit

A simple chatbot using Ollama's LLaMA 3 model, served locally and accessed via a web UI using Streamlit.

## Features
- Chat UI with Streamlit
- Local inference using `ollama` (no internet needed after model download)
- History, prompt input, and responses

## Setup Instructions

### 🔧 Requirements
- Python 3.8+
- Ollama installed and a model gemma3:latest pulled

### 🧪 Run Locally

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run Ollama
ollama run llama3:8b

# Run Streamlit app
streamlit run app.py
