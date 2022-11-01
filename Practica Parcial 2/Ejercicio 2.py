def contadorCaracteres(array):
    contador = 0
    for i in range(len(array)):
        contador = contador + len(array[i])
    
    return contador


def calcularCosto(array2):
    costo = 0
    for i in range(len(array2)):
        for j in range(len(array2[i])):
            if((array2[i][j] >= 'a' and array2[i][j] <= 'z') or (array2[i][j] >= 'A' and array2[i][j] <= 'Z')):
                costo = costo + 100
            elif(array2[i][j] >= '0' and array2[i][j] <= '9'):
                costo = costo + 90
            else:
                costo = costo + 130

    return costo


#Programa Principal
cadena = input("Ingrese un cadena de caracteres: ")
listaSinEspacio = cadena.split()
caracteres = contadorCaracteres(listaSinEspacio)
if(caracteres > 30):
    totalAPagar = calcularCosto(listaSinEspacio) * 0.95
    print(totalAPagar)
elif(caracteres > 50):
    totalAPagar = calcularCosto(listaSinEspacio) * 0.90
    print(totalAPagar)
else:
    totalAPagar = calcularCosto(listaSinEspacio)
    print(totalAPagar)
