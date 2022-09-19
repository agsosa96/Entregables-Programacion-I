#3. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. 
#Luego se solicita imprimir los últimos 10 valores de la lista utilizando segmentación de listas.

def multiplos(valor):
    lista = [valor**2 for valor in range(valor)]

    return lista

def imprimir(lista):
    lista = lista[(len(lista)-10):]
    print(lista)

#Programa principal
numero = int(input("Ingrese un numero para saber sus multiplos del 1 al numero ingresado: "))
if(numero < 10):
    print("No se puede mostrar la lista porque se muestra hasta 10")
else:
    numerosMulti = multiplos(numero)

print(f'La lista de los multiplos es: {numerosMulti}')

imprimir(numerosMulti)
