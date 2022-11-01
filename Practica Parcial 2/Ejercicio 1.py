def paisesEnComun(valor1, valor2):
    return valor1 & valor2


def listaPaisesCompleto(valor1, valor2):
    paisesCompleto = set(valor1 | valor2) 
    
    return paisesCompleto



#Programa Principal
paises = {
    'Oliver': {'Brasil', 'Argentina'},
    'Gabriela': {'Argentina', 'Suiza', 'Uruguay'}
}

print(f"Los paises visitados de Oliver son: {paises['Oliver']}")
print(f"Los paises visitados de Gabriela son: {paises['Gabriela']}")

paisesComun = paisesEnComun(paises['Oliver'], paises['Gabriela'])
paisesCompleto = (listaPaisesCompleto(paises['Oliver'], paises['Gabriela']))

print(f'Los paises en comunes son: {paisesComun}')
print(f'La lista de paises enteros es: {paisesCompleto}')
