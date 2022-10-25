#Realice un programa que pida datos de personas: nombre, día de nacimiento, mes
#de nacimiento, y año de nacimiento. Después deberá repetir lo siguiente:
#preguntar un número de mes y mostrar en pantalla los datos de las personas que
#cumplan los años durante ese mes. Terminará de repetirse cuando se teclee
#vacío en el nombre. Persista y recupere la información en cada ejecución en un
#archivo llamado cumpleaños.json.

import json

listaPersonas = []

nombre = input("Ingrese el nombre: ")
while(nombre != ""):
    personas = {}
    diaNacimiento = int(input("Ingrese el dia de Nacimiento: "))
    mesNacimiento = int(input("Ingrese el mes de Nacimiento: "))
    anioNacimiento = int(input("Ingrese el año de Nacimiento: "))
    

    personas["nombre"] = nombre
    personas["diaNacimiento"] = diaNacimiento
    personas["mesNacimiento"] = mesNacimiento
    personas["anioNacimiento"] = anioNacimiento

    listaPersonas.append(personas)
    nombre = input("Ingrese el nombre: ")

listaPersonasJson = json.dumps(listaPersonas, indent=4)

try:
    contenido = open("archivos/cumpleaños.json", "w")
    contenido.write(listaPersonasJson)
    contenido.close()
except:
    print("No se puede grabar el archivo")

try:
    nuevoContenido = open("archivos/cumpleaños.json", "r")
    lineas = nuevoContenido.read()
    nuevoContenido.close()

    nuevaListaPersonas = json.loads(lineas)
except:
    print("No se encuentra el contenido PA")


mesAEncontrar = int(input("Ingrese el mes a encontrar en el direccionario: "))

for mesAEncontrar in nuevaListaPersonas: 
    print(f'Nombre: {nuevaListaPersonas["nombre"]} Dia de Nacimiento: {nuevaListaPersonas["diaNacimiento"]} Mes de Nacimiento: {nuevaListaPersonas["mesNacimiento"]} Año de Nacimiento: {nuevaListaPersonas["diranioNacimientoeccion"]}')
