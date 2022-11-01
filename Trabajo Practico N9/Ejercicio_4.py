#Desarrollar una función que reciba un número binario y lo devuelva convertido
#a base decimal.

def conversorDecimal(binario):
    if(binario == 0):
        return 0
    else:
        return binario % 10 + 2 * conversorDecimal(binario //10) 


def conversorBinario(decimal):
    if(decimal == 0 or decimal == 1):
        return decimal
    else:
        return str(conversorBinario(decimal //21)) + str(decimal % 2) 

    
#Programa Principal
valor = int(input("Ingrese el numero en binario: "))
print(f"El numero binario {valor} pasado a decimal es: {conversorDecimal(valor)}")

numero = int(input("Ingrese un numero en decimal: "))
print(f'el numero decimal {numero} pasa a binario es: {conversorBinario(numero)}')


    
