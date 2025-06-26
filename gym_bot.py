import openai
import streamlit as st

st.set_page_config(page_title="Gym Chat Coach")
st.title("🏋️‍♂️ Gym Chat Coach")
st.write("Ask me anything about lifting, nutrition, recovery, or gym advice.")

# 🔑 Replace this with your actual OpenAI API key
openai.api_key = "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"

# Input box
user_input = st.text_input("Your question:")

# Generate a response if the user types something
if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a certified personal trainer and expert in fitness, weightlifting, nutrition, and recovery. Give helpful and motivating answers."},
            {"role": "user", "content": user_input}
        ]
    )
    st.write("💬 " + response.choices[0].message["content"])
