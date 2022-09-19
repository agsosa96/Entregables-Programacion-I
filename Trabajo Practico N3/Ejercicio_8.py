#8. Desarrollar una función para reemplazar todas las apariciones de una palabra
#por otra en una cadena de caracteres y devolver la cadena obtenida y un entero
#con la cantidad de reemplazos realizados. Tener en cuenta que sólo deben
#reemplazarse palabras completas, y no fragmentos de palabras. Escribir también
#un programa para verificar el comportamiento de la función.

def cambiarPalabra(lista,cambiarPalabra, palabraCambiada):
    contador = 0
    lista1 = lista.split()
    for i in range(len(lista1)):
        if(lista1[i] == cambiarPalabra):
            lista1[i] = palabraCambiada
            contador += 1

    return lista1 , contador

#Programa Principal
cadena = input("Ingrese su cadena: ") 
palabra = input("ingrese la palabra a cambiar: ") 
cambio = input("Ingrese la palabra por cual va a cambiar: ") 

cadenaFinal, repeticiones = cambiarPalabra(cadena, palabra, cambio)
cadenaFinal = " ".join(cadenaFinal)

print(f'La nueva cadena es {cadenaFinal}')
print(f'La cantidad de repeticiones es {repeticiones}')
