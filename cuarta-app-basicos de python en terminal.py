import streamlit as st
import math, random

st.title("App de ejemplo: Python básico con Streamlit")

# -----------------------------
# 1. VARIABLES Y TIPOS DE DATOS
# -----------------------------
st.header("1️⃣ Nombre y edad")
nombre = st.text_input("¿Cuál es tu nombre?")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, max_value=120, value=25)

if nombre:
    st.write(f"Hola {nombre}, en 2050 tendrás {edad + (2050 - 2025)} años.")

# -----------------------------
# 2. OPERADORES Y CONDICIONALES
# -----------------------------
st.header("2️⃣ Nota y aprobación")
nota = st.number_input(
    "Ingresa tu nota (1 a 7)", min_value=1.0, max_value=7.0, step=0.1
)

if nota >= 4.0:
    st.success("✅ Aprobaste el ramo")
else:
    st.error("❌ No aprobaste")

# -----------------------------
# 3. LISTAS, TUPLAS, SETS Y DICCIONARIOS
# -----------------------------
st.header("3️⃣ Listas, tuplas, sets y diccionarios")
notas = [4.5, 5.0, 3.8]  # lista
nombres = ("Marce", "Ana", "Luis")  # tupla (inmutable)
aprobados = {"Marce", "Ana"}  # set
estudiantes = {"Marce": 5.0, "Ana": 6.2, "Luis": 3.9}  # diccionario

st.write("Notas actuales:", notas)
notas.append(nota)
st.write("Notas con tu nota agregada:", notas)

# -----------------------------
# 4. FUNCIONES
# -----------------------------
def promedio(lista):
    """Calcula el promedio de una lista de números"""
    return sum(lista) / len(lista)

prom = promedio(notas)
st.write(f"El promedio de la clase es: {prom:.2f}")

# -----------------------------
# 5. STRINGS Y MÉTODOS
# -----------------------------
st.header("5️⃣ Manipulación de strings")
texto = "python es divertido"
st.write("Texto en mayúsculas:", texto.upper())
st.write("Texto capitalizado:", texto.capitalize())
st.write("División en palabras:", texto.split())

# -----------------------------
# 6. MÓDULOS (math, random)
# -----------------------------
st.header("6️⃣ Uso de módulos")
raiz = math.sqrt(16)
st.write(f"La raíz cuadrada de 16 es: {raiz}")

aleatorio = random.choice(nombres)
st.write(f"Un estudiante elegido al azar es: {aleatorio}")

# -----------------------------
# 7. DESCARGA DE ARCHIVO
# -----------------------------
st.header("7️⃣ Guardar notas")
contenido = "Notas registradas:\n" + "\n".join(map(str, notas))
st.download_button("Descargar notas.txt", contenido, file_name="notas.txt")

# -----------------------------
# 8. RESUMEN
# -----------------------------
st.header("8️⃣ Resumen")
st.write(f"- Estudiantes: {nombres}")
st.write(f"- Aprobados: {aprobados}")
st.write(f"- Diccionario de notas: {estudiantes}")
