#g. Que compare dos valores y retorne True si el primer argumento es mayor que
#el segundo.

def compararMayor(valorUno, valorDos):
    comparar = lambda x , y : x > y

    return comparar(valorUno, valorDos)

#Programa Principal
numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))
print(f'Devuelve True si el primer valor es mayor: {compararMayor(numeroUno,numeroDos)}')
