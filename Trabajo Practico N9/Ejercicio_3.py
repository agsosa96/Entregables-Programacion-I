#Escribir una función que devuelva la suma de los N primeros números naturales.

def sumaPrimerosNumeros(numero):
    if(numero == 0):
        return 0
    else:
        return sumaPrimerosNumeros(numero - 1) + numero

#Programa Principal
bandera = -100

while(bandera != 0):
    try:
        valor = int(input("Ingrese el tope de la suma: "))
        assert 0 <= valor
        bandera = 0
    except ValueError:
        print("ERROR!!! Ingrese un numero")
    except AssertionError:
        print("ERROR!!! Ingrese solamente numeros naturales")

print(f"La suma de los numeros hasta {valor} es: {sumaPrimerosNumeros(valor)}")
