#Escribir una función que devuelva la cantidad de dígitos de un número entero,
#sin utilizar cadenas de caracteres.

def cantidadEnteros(numero):
    if(numero < 10):
        return 1
    else:
        return cantidadEnteros(numero // 10) + 1

#Programa Principal
bandera = -1000

while(bandera != 0):
    try:
        valor = int(input("Ingrese el numero entero para saber la cantidad de digitos: "))
        assert 0 <= valor
        bandera = 0
    except ValueError:
        print("ERROR!!! Ingrese un numero entero")
    except AssertionError:
        print("ERROR!!! Ingrese un numero natural positivo")

print(f"El cantidad de digitos del numero {valor} es: {cantidadEnteros(valor)}")
