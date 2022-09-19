#1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita
#verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

#a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también
#será un número al azar de dos dígitos. Realice la composición de la lista por comprensión y
#de la forma habitual (tendrá dos funciones distintas).

#b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.

#c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se
#ingresa desde el teclado y la función lo recibe como parámetro. Utilice comprensión de
#listas para resolverlo.

#d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
#auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].


import random


def cargadoDeLista():
    lista = [i for i in range(random.randint(10,99))]
    
    return lista

def cargadoDigitos(carga):
    lista2 = []
    for i in range(0,(len(carga))):
        lista2.append(random.randint(1000,9999))
        
    return lista2

def sumatoria(lista):
    suma = sum(lista)
    
    return suma
 
def eliminado(lista,numero):
    lista3=[lista[i] for i in range(len(lista)) if lista[i] != numero]

    return lista3


def listasCapicua():
    lista = [50, 17, 91, 17, 50]
    if lista == lista[::-1]:
        print("Es capicua")
    else:
        print("No es capicua")


#Programa Principal
lista = cargadoDeLista()
listaDigitos = cargadoDigitos(lista)
print(listaDigitos)
print()

suma = sumatoria(listaDigitos)
print(suma)
print()

listasCapicua()
valor = int(input("Ingrese valor para eliminar: "))
print()
eliminador=eliminado(listaDigitos,valor)
print(eliminador)
    

