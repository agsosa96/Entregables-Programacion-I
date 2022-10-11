#Hacer un programa que registre 10 alumnos y guarde: nombre, nombre de la
#asignatura y 4 notas. Calcular y mostrar el promedio de las notas.

registroAlumnos = []

for i in range(2):
    alumnos = {}
    notas = []
    nombre = input("El nombre del alumno: ")
    asignatura = input("Ingrese el nombre de la asignatura: ")
    for i in range(4):
        nota = int(input("Ingrese la nota de las asignatura: "))
        notas.append(nota)

    alumnos["nombre"] = nombre
    alumnos["asignatura"] = asignatura
    alumnos["notas"] = notas

    registroAlumnos.append(alumnos)

for alumnos in registroAlumnos:
    print(f'Nombre: {alumnos["nombre"]} Alumnos:{alumnos["asignatura"]} Notas: {alumnos["notas"]}')
    print(f'El promedio es: {(sum(alumnos["notas"])/len(alumnos["notas"]))}\n')
