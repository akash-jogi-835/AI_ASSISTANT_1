import streamlit as st
import google.generativeai as genai

st.title("Gemini AI Chatbot")

# Set your Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize model
if "chat" not in st.session_state:
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    st.session_state.chat = model.start_chat()

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.chat.send_message(prompt)
        st.markdown(response.text)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})
