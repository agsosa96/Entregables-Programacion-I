#1. Desarrollar una función que determine si una cadena de caracteres es
#capicúa. Escribir además un programa que permita verificar su funcionamiento
#solicitándole al usuario valores hasta que el mismo sea vacío.


def capicua(lista):
    if(lista == lista[::-1]):
        return True
    else:
        return False

#Programa Principal
cadena = input("Ingrese su cadena de caracteres: ")
while(cadena != ""):
    valor = capicua(cadena)
    if(valor == True):
        print("La cadena de caracteres es CAPICUA")
    else:
        print("La cadena de caracteres NO es CAPICUA")

    cadena = input("Ingrese su cadena de caracteres: ")
