#1. Desarrollar una función para ingresar a través del teclado un número. La
#función rechazará cualquier ingreso inválido de datos utilizando excepciones y
#mostrará la razón exacta del error. Devolver el valor ingresado cuando éste sea
#correcto. Escribir también un programa que permita probar el correcto
#funcionamiento de la misma

def validarDato():
    try:
        numero = int(input("Ingrese un numero: "))
        print("El numero ingresado es correcto")
    except:
        print("Solo se puede ingresar numero enteros")

#Programa Principal
validarDato()
