#c. Que dado un número invierta su signo (de positivo a negativo y viceversa

def invertirSigno(numero):
    invertido = lambda x : x * -1

    return invertido(numero)


#Programa Principal
valor = int(input("Ingrese un numero: "))
print(f'El signo invertido con el numero es: {invertirSigno(valor)}')
