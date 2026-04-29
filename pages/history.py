import streamlit as st

with open("history.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
st.table(content)