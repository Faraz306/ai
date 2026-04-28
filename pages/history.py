import streamlit as st

with open("history.txt", "r") as f:
    content = f.readlines()
st.table(content)