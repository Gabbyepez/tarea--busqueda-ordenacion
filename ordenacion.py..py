# Programa 2: Ordenación de Arreglo Multidimensional

# Definimos una matriz 3x3 con valores desordenados
matriz = [
    [34, 12, 25],
    [9, 67, 45],
    [88, 3, 15]
]

# Convertimos la matriz en una lista
lista = []
for fila in matriz:
    lista.extend(fila)

# Ordenamos la lista
lista_ordenada = sorted(lista)

# Reconstruimos la matriz ordenada (3 columnas)
nueva_matriz = []
n = 3  # número de columnas
for i in range(0, len(lista_ordenada), n):
    nueva_matriz.append(lista_ordenada[i:i+n])

# Mostramos resultados
print("Matriz original:", matriz)
print("Matriz ordenada:", nueva_matriz)