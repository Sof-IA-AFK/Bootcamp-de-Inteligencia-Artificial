"string" #string se utiliza para cadena de textos
'string' #asi tambien podemos generar una string
"Hola mundo"
'Hola mundo'

"""Tus datos son:
Nombre: Sofia
Apellido: Muñoz"""
'''Tus datos son:
Nombre: Sofia
Apellido: Muñoz'''

#En python tenemos diferentes tipos de números
4#Número entero
40.2#Número tipo float
#También tenemos el tipo de datos boolean
True #Verdadero
False #Falso

número = 10 #Primero ejecuta esta linea de código y verás que se imprime el 10 
número = 10+1 #Primero ejecuta esta linea de código y verás que se imprime el 11 
número += 1 #Esta es una forma más cool de hacerlo

#El + adelante del igual significa:
#El valor que ya tienes más lo que esté después del igual


print(número)

número = 10
número += 5 #Entonces 10 + 5 es igual a 15
número -= 5 #Menos 5 nos da10 nuevamente

print(número)


nombre = "Sofia Muñoz"
bienvenida = "Hola " + nombre + " ¿Feliz noche?"

print(bienvenida)



nombre = True
bienvenida = f"Hola  {nombre} ¿Feliz noche?"

print("ola" in bienvenida) #in sirve para ver si una cadena se encuentra dentro de otra

print("Betty" not in bienvenida) #not in sirve para ver si una cadena no se encuentra dentro de otra

print("Hola" not in bienvenida) #in sirve para ver si una cadena se encuentra dentro de otra

#Definiendo una variable
nombre = "Sofia"

#Conectar con +
bienvenida = "Hola " + " ¿Cómo estás?"

#Conectar con f-strings
bienvenida = f"Hola {nombre} ¿Cómo estás?"

#operadores de pertenencia (in / not in)

print("Sofia" in bienvenida) #True
print("Sofia" not in bienvenida) #False


