# lectura y escritura de archivos locales
archivo = "notas.txt"

# Escribir en el archivo
notas = [2.0, 5.0, 3.8]
with open(archivo, "w") as f:
    f.write("Notas registradas:\n")
    for n in notas:
        f.write(str(n) + "\n")

# Leer desde el archivo
with open(archivo, "r") as f:
    contenido = f.read()

print("Contenido del archivo:")
print(contenido)