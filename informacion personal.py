# =====================================================
# Tarea: Trabajando con Diccionarios en Python
# =====================================================

# 1️⃣ Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

print("Diccionario inicial:")
print(informacion_personal)
print("-" * 50)

# 2️⃣ Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"
print("Después de cambiar la ciudad:")
print(informacion_personal)
print("-" * 50)

# 3️⃣ Agregar un nuevo dato (hobby)
informacion_personal["hobby"] = "Fotografía"
print("Después de agregar el hobby:")
print(informacion_personal)
print("-" * 50)

# 4️⃣ Verificar si la clave "telefono" existe, y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número ficticio
print("Después de agregar el teléfono (si no existía):")
print(informacion_personal)
print("-" * 50)

# 5️⃣ Eliminar la clave "edad"
del informacion_personal["edad"]
print("Después de eliminar la edad:")
print(informacion_personal)
print("-" * 50)

# 6️⃣ Imprimir el diccionario final
print("Diccionario final resultante:")
print(informacion_personal)
