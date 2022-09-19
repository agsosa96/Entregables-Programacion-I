#6. Intercalar los elementos de una lista entre los elementos de otra. La
#intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas
#y no se creará una lista nueva sino que se modificará la primera. Por ejemplo,
#si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1,
#9, 3, 7]

def intercalacion(lista1,lista2):
    n = 1
    for i in range(len(lista2)):
        lista1[n:n] = [lista2[i]]
        n += 2
        
    return lista1

prueba1 = [8, 1, 3]
prueba2 = [5, 9, 7]

listaFinal = intercalacion(prueba1,prueba2)

print(f'La lista final queda: {listaFinal}')



