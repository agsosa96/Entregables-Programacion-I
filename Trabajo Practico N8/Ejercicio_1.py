#Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
#usuario y eliminarlos del conjunto mediante el método remove, mostrando el
#contenido del conjunto luego de cada eliminación. Finalizar el proceso al
#ingresar -1. Utilizar manejo de excepciones para evitar errores al intentar
#quitar elementos inexistentes.

import random

def tamanioConjunto():
    bandera = -100
    while(bandera != 0):
        try:
            tamanio = int(input("Ingrese el tamaño del conjunto: "))
            assert 0 < tamanio
            bandera = 0 
        except ValueError:
            print("ERROR!!! Solo se puede ingresar numeros")
        except AssertionError:
            print("ERROR!!! Solo se puede ingresar numeros positivos")


    return tamanio


def valorAzar():
    valor = random.randint(0,9)

    return valor


#Programa Principal
conjunto = set()
numero = tamanioConjunto()

while(numero != len(conjunto)):
    numeroAgregar = valorAzar()
    conjunto.add(numeroAgregar)

quitar = -100
while(quitar != -1):
    try:
        print(conjunto)
        quitar = int(input("Ingrese el numero que quiera quitar: "))
        conjunto.remove(quitar)
    except ValueError:
        print("ERROR!!! Valor ingresado incorrecto")
    except KeyError:
        print("El numero que ingreso no existe")


print(conjunto)
