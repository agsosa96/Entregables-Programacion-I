#5. Escribir una función que reciba una lista como parámetro y devuelva True si
#la lista está ordenada en forma ascendente o False en caso contrario. Por
#ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False.
#Desarrollar además un programa para verificar el comportamiento de la función.

def ordenada(lista):
    lista2 = lista.copy()
    lista2.sort()
    if(lista == lista2):
        return True
    else:
        return False

#Programa Principal
prueba = [1, 2, 3]
valor = ordenada(prueba)

if(valor == True):
    print("La lista esta ordenada de forma ascendete")
else:
    print("La lista no esta ordenada")
