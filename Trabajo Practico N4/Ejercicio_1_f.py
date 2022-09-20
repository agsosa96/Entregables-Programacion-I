#f. Escribe una función que tome dos argumentos: a y b y devuelva la
#multiplicación de ellos.

def multiplicacion(a,b):
    valor = lambda x , y : x * y

    return valor(a,b)

#Programa Principal
numeroUno = int(input("Ingrese el primer numero a multiplicar: "))
numeroDos = int(input("Ingrese el segundo numero a multiplicar: "))
print(f'La multiplicacion de los dos numeros es: {multiplicacion(numeroUno,numeroDos)}')
