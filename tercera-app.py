"""
Mini proyecto: "Gestor de Notas"
Este script muestra los fundamentos de Python paso a paso:
- variables, tipos de datos y operadores
- estructuras de control
- listas, tuplas, diccionarios y sets
- funciones
- manejo de strings
- manejo de archivos
- módulos
"""

# -----------------------------
# 1. VARIABLES Y TIPOS DE DATOS
# -----------------------------
nombre = input("¿Cuál es tu nombre? ")   # string
edad = int(input("¿Cuántos años tienes? "))  # entero

print(f"\nHola {nombre}, en 2050 tendrás {edad + (2050 - 2025)} años.\n")

# -----------------------------
# 2. OPERADORES Y CONDICIONALES
# -----------------------------
nota = float(input("Ingresa tu nota (1 a 7): "))

if nota >= 4.0:
    print("✅ Aprobaste el ramo")
else:
    print("❌ No aprobaste")

# -----------------------------
# 3. LISTAS, TUPLAS, SETS Y DICCIONARIOS
# -----------------------------
notas = [4.5, 5.0, 3.8]  # lista
nombres = ("Marce", "Ana", "Luis")  # tupla (inmutable)
aprobados = {"Marce", "Ana"}  # set (no repite elementos)
estudiantes = {"Marce": 5.0, "Ana": 6.2, "Luis": 3.9}  # diccionario

print("\nNotas actuales:", notas)
notas.append(nota)  # agrega la nueva nota
print("Notas con tu nota agregada:", notas)

# -----------------------------
# 4. FUNCIONES
# -----------------------------
def promedio(lista):
    """Calcula el promedio de una lista de números"""
    return sum(lista) / len(lista)

prom = promedio(notas)
print(f"El promedio de la clase es: {prom:.2f}")

# -----------------------------
# 5. STRINGS Y MÉTODOS
# -----------------------------
texto = "python es divertido"
print("\nTexto en mayúsculas:", texto.upper())
print("Texto capitalizado:", texto.capitalize())
print("División en palabras:", texto.split())

# -----------------------------
# 6. MÓDULOS (ejemplo: math, random)
# -----------------------------
import math, random

raiz = math.sqrt(16)
print(f"\nLa raíz cuadrada de 16 es: {raiz}")

aleatorio = random.choice(nombres)
print(f"Un estudiante elegido al azar es: {aleatorio}")

# -----------------------------
# 7. ARCHIVOS
# -----------------------------
with open("notas.txt", "w") as f:
    f.write("Notas registradas:\n")
    for n in notas:
        f.write(str(n) + "\n")

print("\nSe guardaron las notas en 'notas.txt' ✅")

# -----------------------------
# 8. FINAL: USO DE TODO JUNTO
# -----------------------------
print("\nResumen:")
print(f"- Estudiantes: {nombres}")
print(f"- Aprobados: {aprobados}")
print(f"- Diccionario de notas: {estudiantes}")
