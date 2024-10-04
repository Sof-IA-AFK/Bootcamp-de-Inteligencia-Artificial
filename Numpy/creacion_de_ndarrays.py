import numpy as np

#lista de numeros
numeros = [1, 2, 3, 4, 5]
#creacion de un ndarray a partir de la lista
ndarray_numeros = np.array(numeros)

print(ndarray_numeros)

#Creacion de ndarray a partir de 2x3 con ceros
matriz_ceros = np.zeros((2, 3))

#creacion de un ndarray de 3x3 con unos
matriz_unos = np.ones((3, 3))

#creacion de un ndarray con valores especificos
matriz_personalizada = np.array([[1, 2, 3], [4, 5, 6]])

print(matriz_ceros)
print(matriz_unos)
print(matriz_personalizada)
