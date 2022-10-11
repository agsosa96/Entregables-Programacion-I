#Escriba un programa que ingrese (por teclado) los datos de diez personas
#(nombre, edad, genero, dirección, teléfono), los almacene en un diccionario y
#los muestre. Al realizar dicha muestra, destacar la persona más joven en edad.

listaPersonas = []

for i in range(10):
    personas = {}
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    genero = input("Ingrese el genero con el cual se siente identificado: ")
    direccion = input("Ingrese su direccion: ")
    telefono = input("Ingrese su telefono: ")

    personas["nombre"] = nombre
    personas["edad"] = edad
    personas["genero"] = genero
    personas["direccion"] = direccion
    personas["telefono"] = telefono

    listaPersonas.append(personas)

for personas in listaPersonas:
    print(f'Nombre: {personas["nombre"]} edad: {personas["edad"]} genero: {personas["genero"]} dreccion: {personas["direccion"]} telefono: {personas["telefono"]}')
