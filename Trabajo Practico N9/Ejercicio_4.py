#Desarrollar una función que reciba un número binario y lo devuelva convertido
#a base decimal.

def conversorBinario(numero):
    if(numero == 0):
        return 0
    else:
        if(numero %10 == 1):
            print(numero)
            return conversorBinario(numero //10) + 2 ^ cantidadEnteros(numero)
        else:
            return conversorBinario(numero //10)


def cantidadEnteros(numero1):
    if(numero1 < 10):
        return 1
    else:
        return cantidadEnteros(numero1 // 10) + 1
    
#Programa Principal
valor = int(input("Ingrese el numero en binario: "))
print(f"El numero binario {valor} pasado a decimal es: {conversorBinario(valor)}")
    
