#Operadores númericos
a = 10
b = 3
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

#En Python, el operador de ódulo (%) se utiliza para obtener el residuo de una división 
print("Modulo:", a % b )

#El siguiente signo es el de doble división y el resultado sería la parte entera
print("División entera:", a // b)

#El signo (**) se usa para representar una potenciación
print("Potenciación:", a ** b)

#Queremos sumarle 2 a la variable a, podrías poner a = a + 2 o mejor:
a += 2
print(a)

#Se llama hacer un artificio
a /= 2
print(a)

operation_1 = 2 + 3 * 4
operation_2 = 2 + (3 * 4)
operation_3 = (2 + 3)  * (4 ** 2) / 8 - 1
print(operation_1)
print(operation_2)
print(operation_3)


