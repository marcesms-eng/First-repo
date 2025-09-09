import streamlit as st

# st.title("Calculadora de promedio de notas con evaluaciones que pesan 35% (en dos evaluaciones), 20% y 10%. Nota: usar . antes de los decimales. 🌟")

# Título principal dinámico
st.markdown(
    """
    <h1 style='font-size: 3em; text-align: center;'>
        Calculadora de promedio de notas 🌟
    </h1>
    """,
    unsafe_allow_html=True
)

# Subtítulo con estilo diferente
st.markdown(
    """
    <p style='font-size: 1.1em; color: gray; font-style: italic; text-align: center;'>
        Esta app calcula el promedio considerando dos evaluaciones de 35%, 
        una de 20% y una de 10%. <br>
        Recuerda: usa <b>punto</b> antes de los decimales (ej: 5.5, no 5,5).
    </p>
    """,
    unsafe_allow_html=True
)

# Textos y text boxes
valor1 = st.text_input("Nota evaluación 35%:", key="v1")
valor2 = st.text_input("Nota evaluación 35%:", key="v2")
valor3 = st.text_input("Nota evaluación 20%:", key="v3")
valor4 = st.text_input("Nota evaluación 10%:", key="v4")

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
