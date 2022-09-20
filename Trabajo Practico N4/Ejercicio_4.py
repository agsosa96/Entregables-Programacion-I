#4. Escriba un programa Python para encontrar números divisibles por 3 de una
#lista de números usando Lambda.

def divisiblePorTres(lista):
    listaNueva = []
    multiploTres = lambda x : x %3 == 0
    for i in range(len(lista)):
        if(multiploTres(lista[i]) == True):
            listaNueva.append(lista[i])

    return listaNueva

#Programa Principal
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
listaMultiploTres = divisiblePorTres(lista)
print(f'La lista de los multiplos de 3 son: {listaMultiploTres}')
