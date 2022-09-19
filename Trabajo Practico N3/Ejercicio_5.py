#5.Desarrollar una función que extraiga una subcadena de una cadena de
#caracteres, indicando la posición y la cantidad de caracteres deseada.
#Devolver la subcadena como valor de retorno. Escribir también un programa para
#verificar el comportamiento de la misma. Ejemplo, dada la cadena "El número de
#teléfono es 4356-7890" extraer la subcadena que comienza en la posición 25 y
#tiene 9 caracteres, resultando la subcadena "4356-7890". Escribir una función
#utilizando rebanadas.

def extractora(lista,desde,hasta):
    listaFinal = lista[desde:desde+hasta]

    return listaFinal

#Programa Principal
cadena = str(input("Ingrese su cadena de caracteres: "))
posicion = int(input("ingrese la posicion deseada: "))
cantidad = int(input("ingrese la cantidad de caracteres: "))
cadenaFinal = extractora(cadena, posicion, cantidad)

print(cadenaFinal)
