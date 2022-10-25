#De acuerdo con los siguientes perfiles laborales y las herramientas que debe
#utilizar, cree conjuntos para cada perfil con las herramientas mencionadas.
#Luego, muestre un informe con las mismas de forma individual y especifique cuál
#es son las herramientas que existen en común entre todos los perfiles:

#                                               Herramientas
#Perfil                 Python    R    SQL    Git    Tableau    SAS    Java    Scala
#Científico de datos      X       X     X      X        X        X
#Ingeniero de datos       X             X      X                         X       X
#Desarrollador            X             X      X                         X

#Adicionalmente, identifique cuáles son las herramientas que solo pertenecen a
#un determinado perfil y no está asociado a otro.


cientificoDeDatos = {"Python", "R", "SQL", "Git", "Tableau", "SAS"}
ingenierioDeDatos = {"Python", "SQL", "Git", "Java", "Scala"}
desarrollador = {"Python", "SQL", "Git", "Java"}

print(f"Las herramientas para cientifico de datos son: {cientificoDeDatos}")
print(f"Las herramientas para ingenierio de datos son: {ingenierioDeDatos}")
print(f"Las herramientas desarrollador son: {desarrollador}\n")

print(f"Las herramientas en comun entre cientifico de datos y ingenierio de datos son: {cientificoDeDatos & ingenierioDeDatos}")
print(f"Las herramientas en comun entre cientifico de datos y desarrollador son:{cientificoDeDatos & desarrollador}")
print(f"Las herramientas en comun entre ingenierio de datos y desarrollador son:{ingenierioDeDatos & desarrollador}\n")

print(f"Las herramientas que solo pertenecen a cientifico de datos son: {(cientificoDeDatos - ingenierioDeDatos) - desarrollador}")
print(f"Las herramientas que solo pertenecen a ingenieria de datos son:{(ingenierioDeDatos - cientificoDeDatos) - desarrollador}")
print(f"Las herramientas que solo pertenecen a desarrollador son:{(desarrollador - cientificoDeDatos) - ingenierioDeDatos}\n")

