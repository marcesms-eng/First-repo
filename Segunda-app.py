import streamlit as st

st.title("Calculadora de promedio de notas para ramos con dos evaluaciones 35%, una de 20% y una de 10%. Nota: usar . antes de los decimales. 🌟")

# Textos y text boxes
valor1 = st.text_input("Nota evaluación 35%:", "")
valor2 = st.text_input("Nota evaluación 35%:", "")
valor3 = st.text_input("Nota evaluación 20%:", "")
valor4 = st.text_input("Nota evaluación 10%:", "")

# Botón para calcular
if st.button("Calcular promedio final"):
    try:
        # Convertir a float (si no se puede, usar 0)
        v1 = float(valor1) if valor1 else 0
        v2 = float(valor2) if valor2 else 0
        v3 = float(valor3) if valor3 else 0
        v4 = float(valor4) if valor4 else 0
        
        # Calcular resultado
        resultado = 0.35*v1 + 0.35*v2 + 0.2*v3 + 0.1*v4
        
        st.success(f"El promedio final es: {resultado}")
    except ValueError:
        st.error("Por favor ingresa solo números en las casillas.")