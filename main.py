import streamlit as st


st.set_page_config(page_title="Hello World", page_icon="*", layout="centered")

st.title("Hello World")

name = st.text_input("Enter your name")

if name.strip():
    st.success(f"Hello, {name.strip()}!")
else:
    st.info("Enter your name to see a greeting.")
