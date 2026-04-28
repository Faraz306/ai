import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyBGKjH6F4MoYxW_VnLKSnh7HpaiY7k9uw0")
gemini_model = genai.GenerativeModel('models/gemini-3.1-flash-lite-preview')
st.title("YF Assistant")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        empty, col = st.columns([1, 3])
        with col:
            with st.chat_message("user"):
                st.write(chat["content"])
                with open("history.txt", "a") as f:
                    content_w = f.write(chat["content"])
    else:
        with st.chat_message("assistant"):
            st.write(chat["content"])
            with open("history.txt", "a") as f:
                content_W1 = f.write(chat["content"])
input1 = st.chat_input("Enter anything:")
if input1:
    try:
        response = gemini_model.generate_content(input1)
        ai_response = response.text
        st.session_state.chat_history.append({"role": "user", "content": input1})
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"user | {input1}\n")
            f.write(f"assistant | {ai_response}\n")
        st.rerun()

    except Exception as e:
        st.error(f"An error occurred: {e}")