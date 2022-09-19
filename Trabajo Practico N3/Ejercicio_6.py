# 6.Escribir una función que reciba como parámetro una cadena de caracteres
#en la que las palabras se encuentran #separadas por uno o más espacios.
#Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un
#espacio entre cada una.


def ordenAlfabetico(cadena):
    """Algoritmo que sortea alfabeticamente y deja espacio en cada una"""
    cadena = cadena.split()
    cadena = sorted(cadena)
    return cadena

def conversionCadena(cadenaOrdenada):
    cadenaOrdenada = " ".join(cadenaOrdenada) 
    return cadenaOrdenada


#principal 
cadena = str(input("ingrese una cadena: "))
ordenanza = ordenAlfabetico(cadena)
conversor = conversionCadena(ordenanza)
print(conversor)
