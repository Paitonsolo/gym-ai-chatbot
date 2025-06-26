import openai
import streamlit as st

# Set up page title
st.set_page_config(page_title="🏋️‍♂️ Gym Chat Coach")
st.title("🏋️‍♂️ Gym Chat Coach")
st.write("Ask me anything about lifting, nutrition, recovery, or gym advice.")

# ✅ Securely load your key from Streamlit secrets
client = openai.OpenAI(api_key=st.secrets["openai_key"])

# Get user input
user_input = st.text_input("Your question:")

if user_input:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a certified fitness trainer."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write("💬 " + response.choices[0].message.content)
    except Exception as e:
        st.error(f"❌ Error: {e}")
