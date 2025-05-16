import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"  # Replace with your Flask API URL

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("🤖 Chat with My Flask Bot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="input_text")
    submit = st.form_submit_button("Send")

# Function to call Flask API
def get_bot_response(message):
    try:
        response = requests.post(API_URL, json={"query": message})
        return response.json().get("response", "No response from bot.")
    except Exception as e:
        return f"Error: {e}"

# On form submit
if submit and user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_reply = get_bot_response(user_input)
    st.session_state.chat_history.append(("Bot", bot_reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
