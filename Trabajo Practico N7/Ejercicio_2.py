#Escriba un programa que ingrese (por teclado) los datos de diez personas
#(nombre, edad, genero, dirección, teléfono), los almacene en un diccionario y
#los muestre. Al realizar dicha muestra, destacar la persona más joven en edad.

listaPersonas = []
numeroMasJoven = 1000
masJoven = {}

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

    if(numeroMasJoven > personas["edad"]):
        numeroMasJoven == personas["edad"]
        masJoven["nombre"] = nombre
        masJoven["edad"] = edad
        masJoven["genero"] = genero
        masJoven["direccion"] = direccion
        masJoven["telefono"] = telefono

for personas in listaPersonas:
    print(f'Nombre: {personas["nombre"]} edad: {personas["edad"]} genero: {personas["genero"]} direccion: {personas["direccion"]} telefono: {personas["telefono"]}\n')

print(f'El nombre de la persona mas joven es: {masJoven["nombre"]} edad: {masJoven["edad"]} genero: {masJoven["genero"]} dreccion: {masJoven["direccion"]} telefono: {masJoven["telefono"]}')

