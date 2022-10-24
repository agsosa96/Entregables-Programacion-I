#Crear tres conjuntos:

#Pares: valores pares entre 0 y 100
#Impares: valores impares entre 0 y 100
#Azar: 50 valores al azar entre 0 y 100

#Una vez generados los tres conjuntos, deberá realizar las siguientes acciones:

#Generar dos nuevos  conjuntos: uno con la intersección entre azar y pares; y
#azar e impares. Informe de cada uno de ellos: la cantidad, el valor máximo y
#mínimo.


import random

def crearConjuntoParesEImpares(tamanio):
    pares = set()
    impares = set()
    while(len(pares) != tamanio or len(impares) != tamanio):
        valor = random.randint(0,100)
        if(valor %2 == 0 and len(pares) != tamanio):
            pares.add(valor)
        elif(valor %2 != 0 and len(impares) != tamanio):
            impares.add(valor)

    return pares, impares

def crearConjuntoAzar():
    azar = set()
    while(len(azar) != 50):
        numero = random.randint(0,100)
        azar.add(numero)
        
    return azar


#Programa Principal
bandera = -100
while(bandera != 0):
    try:
        numero = int(input("Ingrese el tamanio del conjunto: "))
        assert 0 <= numero <= 50 
        conjuntoPares, conjuntoImpares = crearConjuntoParesEImpares(numero)
        conjuntoAzar = crearConjuntoAzar()
        bandera = 0
    except ValueError:
        print("ERROR!!! Solo se puede ingresar numeros")
    except AssertionError:
        print("ERROR!!! El valor del rango tiene que ser entre 0 y 50")

print(f'El conjunto de pares es: {conjuntoPares}\n')
print(f'El conjunto de impares es:{conjuntoImpares}\n')
print(f'El conjunto al azar es: {conjuntoAzar}\n')


interseccion1 = (conjuntoAzar & conjuntoPares)
interseccion2 = (conjuntoAzar & conjuntoImpares)

print(f"La interseccion entre los pares y azar es: {interseccion1}")
print(f"El valor minimo es: {min(interseccion1)}")
print(f"El valor maximo es: {max(interseccion1)}\n")
print(f"La interseccion entre los impares y azar es: {interseccion2}")
print(f"El valor minimo es: {min(interseccion2)}")
print(f"El valor maximo es: {max(interseccion2)}\n")

 






