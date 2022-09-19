#2. Realizar una función que reciba como parámetros dos cadenas de caracteres
#conteniendo números reales, sume ambos valores y devuelva el resultado como un
#número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
#utilizando manejo de excepciones para detectar el error.

def sumaCadena(listaUno, listaDos):
    try:
        sumador = float(listaUno) + float(listaDos)
        return sumador
    except:
        return -1


#Programa Principal
cadenaUno = input("Ingrese el primer numero: ")
cadenaSegundo = input("Ingrese el segundo numero: ")
sumador = sumaCadena(cadenaUno, cadenaSegundo)

if(sumador == -1):
    print("Tiene un caracter que no corresponde a la suma")
else :     
    print(f'La de las cadenas es: {sumador}')
