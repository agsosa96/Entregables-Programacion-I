#5. Escribir un programa que juegue con el usuario a adivinar un número. El
#programa debe generar un número al azar entre 1 y 500 y el usuario debe
#adivinarlo. Para eso, cada vez que se introduce un valor se muestra un mensaje
#indicando si el número que tiene que adivinar es mayor o menor que el
#ingresado. Cuando consiga adivinarlo, se debe imprimir en pantalla la cantidad
#de intentos que le tomó hallar el número. Si el usuario introduce algo que no
#sea un número se mostrará un mensaje en pantalla y se lo contará como un
#intento más.

import random

def adivinarNumero(valor):
    intentos = 0
    while(True):
        try:
            numero = int(input("Ingrese el numero que crees que es: "))
            if(valor == numero):
                return intentos
            elif(valor < numero):
                print("El numero a adivinar es mas chico")
                intentos += 1
            elif(valor > numero):
                print("El numero a adivinar es mas grande")
                intentos += 1
        except ValueError:
            intentos += 1
            print("Solo se puede ingresar numero enteros")
                             
#Programa Principal
numero = random.randint(1,50)
print(numero)
numeroAdivinado = adivinarNumero(numero)
print(f'El numero de intentos es: {numeroAdivinado}')

