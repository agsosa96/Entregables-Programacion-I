#4. El método index permite buscar un elemento dentro de una lista, devolviendo
#la posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista
#se produce una excepción de tipo ValueError. Desarrollar un programa que cargue
#una lista con números enteros ingresados a través del teclado (terminando con
#-1) y permita que el usuario ingrese el valor de algunos elementos para
#visualizar la posición que ocupan, utilizando el método index. Si el número no
#pertenece a la lista se imprimirá un mensaje de error y se solicitará otro para
#buscar. Abortar el proceso al tercer error detectado. No utilizar el operador
#in durante la búsqueda.

def cargaLista(lista):
    numero = int(input("Ingrese el numero que quiere ingresar en la lista (Termina con -1): "))
    while(numero != -1):
        lista.append(numero)
        numero = int(input("Ingrese el numero que quiere ingresar en la lista (Termina con -1): "))
    
    return lista

def verificacion(lista):
    contador = 0
    while(True):
        valor = int(input("Ingrese el numero para saber la posicion: "))
        try:
            print(f'La posicion en la que se encuentra el numero es: {lista.index(valor)}')
        except ValueError:
            contador += 1
            if(contador == 3):
                return -1
            print("El numero no exite intente nuevamente")
            

#Programa Principal
listaACargar = []
listaCargada = cargaLista(listaACargar)
intentos = verificacion(listaCargada)
if(intentos == -1):
    print("Exediste los intentos maximos que son 3")

