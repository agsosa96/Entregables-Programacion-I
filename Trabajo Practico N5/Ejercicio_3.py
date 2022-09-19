#3. Desarrollar una función que devuelva una cadena de caracteres con el nombre.
#del mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
#obtenerse de una lista de cadenas de caracteres inicializada dentro de la
#función. Devolver una cadena vacía si el número de mes es inválido. La
#detección de meses inválidos deberá realizarse a través de excepciones.

def pedirDato():
    while(True):
        try:
            dato = int(input("Ingrese un numero entre 1 y 12: "))
            assert 1 <= dato <= 12
            return dato
        except AssertionError:
            print("El numero ingresado tiene que estar entre 1 y 12")
        except ValueError:
            print("El valor ingresado tiene que ser un entero")

def nombreMes(valor):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    return meses[valor-1]

#Programa Principal
numero = pedirDato()
print(f'El {numero} es el mes {nombreMes(numero)}')
