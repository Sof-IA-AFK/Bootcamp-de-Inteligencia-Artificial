a = 5
b = 8
c = a + b
print(c)
nombre = "Sofia"
nombre = "Cathalina"
nombre = "Sofia Muñoz"
#Podemos concluir que las variables son modificables
print(nombre)

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
número -= 5 #Menos 5 nos da 10 nuevamente

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

#Definiendo una variable con CamelCase (Recomendado para Javascript)
nombreCompletoDeTuProfe = "Jheyson Galvis" #CamelCase sirve para definir variables

#Definiendo una variable con SnakeCase (Recomendado para Python)
nombre_completo_de_tu_profe = "Jheyson Galvis " #Snake Case
