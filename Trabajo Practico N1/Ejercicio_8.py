#8. Generar e imprimir una lista por comprensión entre A y B con los múltiplos
#de 7 que no sean múltiplos de 5. A y B se ingresan desde el teclado.

def comprension(desde,hasta):
    lista = [numero for numero in range(desde,hasta) if numero %7 == 0 and numero %5 != 0]

    return lista

#Programa Principal
valorInicial = int(input("ingrese valor inicial: "))
valorFinal = int(input("ingrese valor final: "))
listaFinal =  comprension(valorInicial,valorFinal)
print(listaFinal)
