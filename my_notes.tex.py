# ==========================================
# Tarea: Trabajo con Archivos de Texto en Python
# ==========================================

# 1. Escritura de Archivo de Texto
# Creamos (o sobrescribimos) un archivo llamado "my_notes.txt"
# y escribimos en él tres notas personales.

# Abrimos el archivo en modo escritura ("w")
archivo = open("my_notes.txt", "w")

# Escribimos varias líneas de notas
archivo.write("Nota 1: Hoy estoy aprendiendo a trabajar con archivos en Python.\n")
archivo.write("Nota 2: La práctica es fundamental para mejorar en programación.\n")
archivo.write("Nota 3: Subiré este archivo a mi repositorio en GitHub.\n")

# Cerramos el archivo después de escribir
archivo.close()

# ------------------------------------------

# 2. Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ("r")
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea con readline()
print("Contenido del archivo my_notes.txt:\n")
linea = archivo.readline()   # lee la primera línea

while linea != "":           # mientras no lleguemos al final
    print(linea.strip())     # mostramos en consola (quitamos salto de línea con strip)
    linea = archivo.readline()  # leemos la siguiente línea

# ------------------------------------------

# 3. Cierre de Archivos
archivo.close()
print("\nEl archivo ha sido cerrado correctamente.")
