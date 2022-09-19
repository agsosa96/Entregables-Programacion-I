#4. Eliminar de una lista de palabras las palabras que se encuentren en una
#segunda lista. Imprimir la lista original, la lista de palabras a eliminar y
#la lista resultante.

def eliminoRepetidas(lista1,lista2):
    repetidas = []
    for i in lista2:
        if i in lista1:
            repetidas.append(i)
            lista1.remove(i)
    return repetidas, lista1

prueba1 = ["hola", "como", "estas", "todo", "bien"]
prueba2 = ["hola", "como", "estas"]

copia_prueba1 = prueba1.copy()

rep, res = eliminoRepetidas(copia_prueba1, prueba2)

print("La lista original es:", prueba1)
print("La lista resultante es:", res)
print("La lista repetida es:", rep)

