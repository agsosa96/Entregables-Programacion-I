#Crear dos conjuntos con cinco valores generados al azar, que se encuentre entre
#1 y 10. Al finalizar, realizar:

#Mostrar los valores que son en común entre ambos conjuntos

#Luego, volcar desde el primer conjunto al segundo, aquellos valores que no se
#encuentran del primero en el segundo

import random

def crearConjunto(tamanio):
    conjunto = set()
    while(tamanio != len(conjunto)):
        numero = random.randint(1,10)
        conjunto.add(numero)

    return conjunto

#Programa Principal
conjunto1 = crearConjunto(5)
conjunto2 = crearConjunto(5)

print(f"El primer conjunto es: {conjunto1}")
print(f"El segundo conjunto es: {conjunto2}")

interseccion = conjunto1 & conjunto2

print(f"Los valores comunes son: {interseccion}")

diferencia = conjunto2 - conjunto1

print(f"La diferencia entre el primer conjunto y el segundo conjunto es: {diferencia}")
