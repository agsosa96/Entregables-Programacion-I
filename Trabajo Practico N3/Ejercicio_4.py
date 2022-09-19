# 4. Escribir una función filtrarPalabras() que reciba una cadena de caracteres
#conteniendo una frase y un entero N, y devuelva otra cadena con las palabras
#que tengan N o más caracteres de la cadena original. Escribir también un
#programa para verificar el comportamiento de la misma.

def filtrarPalabras(frase1,entero1):
    lista = frase1.split()
    listaFinal = [lista[i] for i in range(len(lista)) if(len(lista[i]) >= entero1)]
    
    return listaFinal


#Programa Principal
frase = input("Ingrese su frase: ")
entero = int(input("Ingrese su entero: "))
palabrasFinal = filtrarPalabras(frase,entero)
print(palabrasFinal)
