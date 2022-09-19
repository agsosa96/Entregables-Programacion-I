#2. Escribir funciones para:

#a. Generar una lista de 50 números aleatorios del 1 al 100. Utilice comprensión
#de listas para generar el resultado.

#b. Recibir una lista como parámetro y devolver True si la misma contiene algún
#elemento repetido. La función no debe modificar la lista.

#c. Recibir una lista como parámetro y devolver una nueva lista con los
#elementos únicos de la lista original, sin importar el orden.

#Combinar estas tres funciones en un mismo programa


import random

def genercionLista():
    lista=[random.randint(1,100) for i in range(0,50)]
    return lista

def funcionTrue(lista):
    if len(lista) != len(set(lista)):
        return True
    else:
        return False

listaG = genercionLista()
print(listaG)

lista = [1,2,3,4,4,4]
valor = funcionTrue(lista)
print(valor)
    
