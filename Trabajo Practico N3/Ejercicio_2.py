#2. Leer una cadena de caracteres e imprimirla sin espacios en sus laterales.

def quitarEspacios(lista):
    lista = lista.lstrip()
    lista = lista.rstrip()

    return lista

#Programa Principal
cadena = input("Ingrese su cadena: ")
print(f'Su cadena sin espacio es: {quitarEspacios(cadena)}')
