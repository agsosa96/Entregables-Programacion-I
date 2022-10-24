#Desarrollar una función que devuelva el producto de dos números enteros por
#sumas sucesivas.

def sumaConsecutiva(numero1, numero2):
    if(numero2 == 0):
        return 0
    else:
        return sumaConsecutiva(numero1, numero2 - 1) + numero1

#Programa Principal
bandera = -100

while(bandera != 0):
    try:
        valor1 = int(input("Ingrese el primer numero: "))
        valor2 = int(input("Ingrese el segundo numero: "))
        assert 0 <= valor1
        assert 0 <= valor2
        bandera = 0
    except ValueError:
        print("ERROR!!! Ingrese solo numeros enteros")
    except AssertionError:
        print("ERROR!!! Ingrese numero enteros")

print(f"La suma consecutiva de {valor1} y {valor2} es: {sumaConsecutiva(valor1, valor2)}")
        
