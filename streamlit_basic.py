import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os  

with st.sidebar:
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)

    st.title("Chat with GPT-4o")
    st.write("Enter your message below and press 'Send' to chat with the AI.")

    user_input = st.text_input("Your message:", "")
    if st.button("Send"):
        if user_input:
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
            response = client.chat.completions.create(
                model="gpt-4o",
                temperature=0.9,
                messages=messages
            )
            ai_response = response.choices[0].message.content
            st.write(f"AI: {ai_response}")
        else:
            st.warning("Please enter a message before sending.")