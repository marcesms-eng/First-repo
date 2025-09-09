import streamlit as st

st.title("Primera Web App de Marcee con cambios directo en Github! 🌍")

name = st.text_input("¿Cómo te llamas?")
if name:
    st.write(f"Hola {name}!")
