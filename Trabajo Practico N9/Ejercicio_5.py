#Escriba un programa utilizando recursividad, pueda retornar la multiplicación
#mediante el Método ruso, que consiste en:

#•Escribir los números (A y B) que se desea multiplicar en la parte superior de
#sendas columnas.

#•Dividir A entre 2, sucesivamente, ignorando el residuo, hasta llegar a la
#unidad. Escribir los resultados en la columna A.

#•Multiplicar B por 2 tantas veces como veces se ha dividido A entre 2. Escribir
#los resultados sucesivos en la columna B.0

#•Sumar todos los números de la columna B que estén al lado de un número impar
#de la columna A. Éste es el resultado.


def multiplicacionRusa(numero1, numero2):
    if(numero1 == 0):
        return 0
    else:
        if(numero1 %2 != 0):
            print(f"{numero1}\t{numero2}\t{numero2}")
            return multiplicacionRusa(numero1 // 2 , numero2 * 2) + numero2
        else:
            print(f"{numero1}\t{numero2}")
            return multiplicacionRusa(numero1 // 2 , numero2 * 2)


#Programa Principal
bandera = -100

while(bandera != 0):
    try:
        valor1 = int(input("Ingrese el primer numero a multiplicar: "))
        valor2 = int(input("Ingrese el segundo numero a multiplicar: "))
        bandera = 0
    except ValueError:
        print("ERROR!!! Ingrese un numero")

print(f"A\tB\tSumando")
print(f"Resultado: {multiplicacionRusa(valor1, valor2)}")    
            
