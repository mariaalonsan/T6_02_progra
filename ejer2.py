"""
Escribe una función normalizar_filas que reciba una matriz de NumPy como argumento y normalize cada fila dividiendo todos los elementos de cada fila por la suma de los elementos de la misma fila.
"""

import numpy as np

# Definimos de la función
def normalizar_filas(matriz):
    # Suma de cada fila
    suma_filas = matriz.sum(axis=1, keepdims=True)
    # Divide cada elemento de la fila por la suma de su fila
    return matriz / suma_filas

# Ejemplo de uso de la función
matriz_ejemplo = np.array([[8, 2, 3], [4, 3, 9], [0, 8, 1]])

# Llamamos a la función y printeamos el resultado
resultado_normalizado = normalizar_filas(matriz_ejemplo)
print(resultado_normalizado)
