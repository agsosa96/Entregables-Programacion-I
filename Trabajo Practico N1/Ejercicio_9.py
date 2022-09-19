#9. Generar una lista con 50 números al azar entre 1 y 100 y crear una nueva
#con los elementos de la primera que sean impares. El proceso deberá realizarse
#utilizando listas por comprensión. Imprimir las dos listas por pantalla.

import random

lista1 = [random.randint(1,100) for i in range(0,50)]
lista2 = [lista1[i] for i in range(len(lista1)) if lista1[i] %2 != 0]

print(lista1)
print()
print(lista2)


