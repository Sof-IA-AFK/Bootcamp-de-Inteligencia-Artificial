import numpy as np

#creacion de un ndarray en 2d
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
#acceso a un elemnto especifico de la fila 1, columna 2
elemento = matriz[1, 2]
print(elemento)

#seleccion de una fila (fila 0)
fila = matriz[0, :]
print(fila)

#Selección de una columna (columna 1)
columna = matriz[:, 1]
print(columna)
