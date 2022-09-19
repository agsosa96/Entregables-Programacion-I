#7. Desarrollar una función que devuelva una subcadena con los últimos N
#caracteres de una cadena dada. La cadena y el valor de N se pasan como
#parámetros.


def leoCadena(cadena, cant):
    nueva_cadena = cadena[-cant:]
    return nueva_cadena


#Programa Principal
cadena = input("Ingrese la cadena: ")
valor= int(input("Ingrese el valor de n: "))
devolucionSub = leoCadena(cadena,valor)
print(devolucionSub)
