#b. Determine si una nota esta aprobada o no (mayor o igual que 4 aprueba). Retorna True por aprobado; False por desaprobado.

def estadoNota(lista):
    resultado = []
    aprobado = lambda x : x >= 4
    for i in range(len(lista)):
        resultado.append(aprobado(lista[i]))

    return resultado

#Programa Principal
notas = [4, 2, 5, 7, 8, 10, 9, 6]
print(notas)
notaResultado = estadoNota(notas)
print(f'El resultado de las notas es: {notaResultado}')
