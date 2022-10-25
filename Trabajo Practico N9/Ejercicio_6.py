#Explique cuál es el objetivo de la siguiente función. Realice una explicación y
#verifique los resultados.

#def f(x):
#   if(x > 100):
#       return (x - 10)
#   else:
#       return (f(f(x + 11)))

def f(x):
   if(x > 100):
       return (x - 10)
   else:
       return (f(f(x + 11)))


print(f(102))
