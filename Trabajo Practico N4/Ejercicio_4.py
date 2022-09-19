#4.Escriba un programa Python para encontrar números divisibles por 3 de una
#lista de números usando Lambda

listita = [1,2,3,6,12,29]

def contador(mama):
    lista2 = []
    multiploTres= lambda x:x %3 == 0
    for i in range(len(mama)):
        if(multiploTres(mama[i]) == True): 
            lista2.append(mama[i])
    return lista2

print(contador(listita))
