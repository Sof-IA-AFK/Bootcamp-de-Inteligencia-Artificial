import numpy as np

#Creacion de ndarray con valores del 0 al 9 din incluir el 10
numeros_1 = np.arange(0, 10)
print(numeros_1)

#creación de ndarray con valores del 1 al 5 de dos en dos
numeros_2 = np.arange(1,6, 2) 
print(numeros_2)

#creación de ndarrays con valres del 0 al 4, sin incluir el 4 de 0.5 en 0.5
numeros_3 = np.arange(0,4, 0.5)
print(numeros_3)

#creación de un ndarray con diez valores espaciados uniformemente entre 0 y 1
puntos_1 = np.linspace(0, 1, 10)
print(puntos_1)

puntos_2 = np.linspace(2, 10, 5)
print(puntos_2)

#Creacion de un ndarray de 3x3 con numeros aleatorios entre 0 y 1
matriz_aleatoria_1 = np.random.rand(3, 3)
print(matriz_aleatoria_1)

#creacion de un ndarray de 5 elementos con numeros aleatorios entre 0 y 1
vector_aleatorio_1 = np.random.rand(5)
print(vector_aleatorio_1)

