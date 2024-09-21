# El primer tipo de dato compuestos será la lista

lista = ["Sofia Muñoz", "Who is Sofi?", True, 1.50]
print(lista)
# En el mundo de la programación no contamos del 1 al 10, contamos del 0 al 10
print(lista[0])
lista[0] = "Choco"
print(lista[0])

#La tupla es una lista que no se puede modificar
tupla = ("Cereales de chocolate", "Yogurt", "galleta integral", False, 8.50)
print(tupla[1])
#tupla[1] = "Cereales frutloops"
#print(tupla[1])

# Creando un conjunto set
# El conjunto no admite elementos duplicados
conjunto = {"Sofia Muñoz", "Who is Sofi?", True, 1.50, "Sofia Muñoz", "celular 3233923770"}
print(conjunto)
#Creando un enunciado
print(f"El conjunto es: {conjunto}")

# Creando un diccionario
# Estructura "clave": valor
diccionario = {
    "nombre": "Sofia", 
    "apellidos": "Muñoz", 
    "estatura": 1.50,
    "está feliz": True,
    "nombre": "Sofia",
    "edad": 20
}
print(diccionario)

print(diccionario["nombre"])
print(diccionario["apellidos"])
print(diccionario["está feliz"])
print(diccionario["estatura"] + 2) #3.50
print(diccionario["edad"])

