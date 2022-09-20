#2. Escriba un programa para generar una función (utilizando filter) y lambdas
#para separar los números pares e impares de una lista de números. La función
#debe retornar dos valores resultantes.


def separarPares(lista):
    pares = list(filter(lambda x:x %2 == 0, lista))
    impares = list(filter(lambda x:x %2 != 0, lista))
    
    return pares, impares

#Programa Principal
listaASeparar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listaASeparar)
listaUno, listaDos = separarPares(listaASeparar)
print(f'La lista de pares es: {listaUno}')
print(f'La lista de los impares es: {listaDos})
