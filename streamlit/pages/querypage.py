import streamlit as st
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

# Helper function to initialize LLM
def initialize_llm(model_name: str):
    return Ollama(model=model_name, base_url="http://ollama-ollama-1:11434", verbose=True)

# Helper function to handle sending prompts
def send_prompt(llm, prompt):
    response = llm.invoke(prompt)
    return response

# Streamlit App
st.title("Chat with Ollama")

# Initialize session state for messages and selected model
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question!"}
    ]

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "phi:latest"

# Model selection
available_models = ["phi:latest", "gemma2", "mistral"]  # Extend this list as needed
selected_model = st.selectbox("Choose a model:", available_models, index=0)

# Update the model in session state if it changes
if selected_model != st.session_state.selected_model:
    st.session_state.selected_model = selected_model
    st.session_state.messages.append(
        {"role": "assistant", "content": f"Switched to model: {selected_model}"}
    )

# Initialize the LLM based on the selected model
llm = initialize_llm(st.session_state.selected_model)

# Input for user prompt
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Generate a response if the last message is from the user
if st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = send_prompt(llm, st.session_state.messages[-1]["content"])
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error generating response: {e}")
