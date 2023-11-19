"""
1) Implementa una función llamada elementos_mayores que tome una matriz de NumPy y un número x como argumentos. La función debe devolver una nueva matriz que contenga solo los elementos mayores que x
"""
import numpy as np

# Vamos a definir de la función
def elementos_mayores(matriz, x):
    # Filtramos los elementos de la matriz que son mayores que x
    return matriz[matriz > x]

# Ejemplo de uso de la función
matriz_ejemplo = np.array([[7, 2, 5], [1, 8, 6], [5, 5, 3]])
x = 4

# Y llamamos a la función y printeamos el resultado
resultado = elementos_mayores(matriz_ejemplo, x)
print(resultado)
