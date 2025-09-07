import streamlit as st

st.title("Calculadora de Porcentajes 🌟")

# Textos y text boxes
valor1 = st.text_input("Primer 35%:", "")
valor2 = st.text_input("Segundo 35%:", "")
valor3 = st.text_input("Tercer 20%:", "")
valor4 = st.text_input("Cuarto 10%:", "")

# Botón para calcular
if st.button("Calcular"):
    try:
        # Convertir a float (si no se puede, usar 0)
        v1 = float(valor1) if valor1 else 0
        v2 = float(valor2) if valor2 else 0
        v3 = float(valor3) if valor3 else 0
        v4 = float(valor4) if valor4 else 0
        
        # Calcular resultado
        resultado = 0.35*v1 + 0.35*v2 + 0.2*v3 + 0.1*v4
        
        st.success(f"El resultado final es: {resultado}")
    except ValueError:
        st.error("Por favor ingresa solo números en las casillas.")