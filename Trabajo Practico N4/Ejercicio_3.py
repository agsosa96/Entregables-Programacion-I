#3. Escriba un programa para contar los números pares e impares en una lista
#dada de enteros usando Lambda.

def contadorPares(lista):
    contadorPar = 0
    contadorImpar = 0
    for i in range(len(lista)):
        reconocedorPar = lambda x : x %2 == 0
        if(reconocedorPar(lista[i]) == True):
            contadorPar += 1
        else:
            contadorImpar += 1
    
    return contadorPar, contadorImpar

#Programa Principal
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
pares, impares = contadorPares(lista)
print(f'La cantidad de pares que hay en la lista es: {pares}')
print(f'La cantidad de impares que hay en la lista es: {impares}')
