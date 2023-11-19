"""
Crea una función multiplicar_matrices que reciba dos matrices de NumPy A y B, y devuelva el producto matricial de ambas
"""
import numpy as np

# Definimos de la función
def multiplicar_matrices(A, B):
    # Realizamos el producto matricial de A y B
    return np.dot(A, B)

# Ejemplo de uso de la función
A = np.array([[8, 5], [6, 2]])
B = np.array([[5, 6], [3, 7]])

# Por último llamamos a la función y printeamos el resultado
resultado_producto = multiplicar_matrices(A, B)
print(resultado_producto)
