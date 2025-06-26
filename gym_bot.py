import openai
import streamlit as st

# Set page title and intro
st.set_page_config(page_title="🏋️‍♂️ Gym Chat Coach")
st.title("🏋️‍♂️ Gym Chat Coach")
st.write("Ask me anything about lifting, nutrition, recovery, or gym advice.")

# ✅ Your OpenAI key (be careful—this is public if shared)
client = openai.OpenAI(
    api_key="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"
)

# Get user input
user_input = st.text_input("Your question:")

if user_input:
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a certified fitness trainer."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write("💬 " + response.choices[0].message.content)
    except Exception as e:
        st.error(f"❌ Error: {e}")
