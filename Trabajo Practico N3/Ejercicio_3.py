#3. Los números de claves de dos cajas fuertes están intercalados dentro de un
#número entero llamado "clave maestra", cuya longitud no se conoce. Realizar un
#programa para obtener ambas claves, donde la primera se construye con los
#dígitos ubicados en posiciones impares de la clave maestra y la segunda con los
#dígitos ubicados en posiciones pares. Los dígitos se numeran desde la
#izquierda. Ejemplo: Si clave maestra fuera 18293, la clave 1 sería 123 y la
#clave 2 sería 89.

def desencriptado(lista):
    lista1 = [lista[i] for i in range(len (lista)) if (i %2 == 0)]
    lista2 = [lista[i] for i in range(len (lista)) if (i %2 != 0)]

    return lista1 , lista2

#Programa Principal

claveMaestra = int(input("Ingrese su clave: "))
arrayClave=str(claveMaestra)
clave1, clave2 = desencriptado(arrayClave)

clave1 = "".join(clave1)
clave2 = "".join(clave2)

print(f'La primera clave es: {clave1}')
print(f'La secundaria clave es: {clave2}')

 

