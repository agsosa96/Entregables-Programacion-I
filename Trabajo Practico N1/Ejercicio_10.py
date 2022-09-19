#10. Resolver el siguiente problema, diseñando las funciones a utilizar:

#Una clínica necesita un programa para atender a sus pacientes. Cada paciente
#que ingresa se anuncia en la recepción indicando su número de afiliado (número
#entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un
#0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de
#socio. Luego se solicita:

#a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
#los pacientes atendidos por turno en el orden que llegaron a la clínica.

#b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
#atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta que se
#ingrese -1 como número de afiliado.

#Programa Principal
urgencia = []
turno = []

afiliado = int(input("Ingrese el numero de afiliado: "))

while(afiliado != -1):
    if(afiliado < 0 or afiliado > 10000):
        print("Numero de afiliado invalido, intentelo nuevamente")
        afiliado = int(input("Ingrese el numero de afiliado: "))
    else:
        valor = int(input("Ingrese un 0 si viene por urgencia || Ingrese un 1 si viene por turno: "))
        if(valor == 0):
            urgencia.append(afiliado)
        else:
            turno.append(afiliado)
        afiliado = int(input("Ingrese el numero de afiliado: "))

print(f'La lista por urgencia es {urgencia}') 
print(f'La lista por turrno es {turno}')   
        
        
    
