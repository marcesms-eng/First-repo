import streamlit as st

st.title("Hello, world! 🌍")

name = st.text_input("¿Cómo te llamas boludo?")
if name:
    st.write(f"Hola {name}, mono peludo!")