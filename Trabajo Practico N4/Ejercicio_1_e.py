#e. Dado un valor numérico retorne True si es positivo o cero; False en caso
#contrario.

def mayorACero(numero):
    mayor = lambda x : x >= 0

    return mayor(numero)

#Programa Principal
valor = int(input("Ingrese el numero que quiera saber si es mayor a cero: "))
print(f'Devuelve True si el numero es mayor o igual a cero: {mayorACero(valor)}')
