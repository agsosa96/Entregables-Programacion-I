#d. Que dado un nombre determine si su longitud es larga (mayor de 10
#caracteres). Retorna True o False.

def determinarLongitud(caracter):
    longitud = lambda x : x > 10

    return longitud(len(caracter))

#Programa Principal
listaCaracteres = input("Ingrese el nombre para saber si es largo: ")
print(f'Devuelve True si el nombre es mayor a 10: {determinarLongitud(listaCaracteres)}')
