import streamlit as st
from utils import call_gemini_api

# Streamlit app
st.title("Sales Expert Chatbot using Gemini API")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_input")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    bot_response = call_gemini_api(user_input)
    st.session_state.messages.append({"user": user_input, "bot": bot_response})

with st.chat_message("AI Bot"):
    st.write("Hello 👋, Do you have any car sales questions?")

# Display conversation
for message in st.session_state.messages:
    with st.chat_message("user"):
        st.write(f"You: {message['user']}")
    with st.chat_message("AI Bot"):
        st.write(f"AI Sales Expert: {message['bot']}")
