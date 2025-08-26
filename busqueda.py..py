# Programa 1: Búsqueda en Arreglo Multidimensional

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición si lo encuentra
    return None  # Si no lo encuentra

# Probamos la función
valor_buscado = 50
resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz")