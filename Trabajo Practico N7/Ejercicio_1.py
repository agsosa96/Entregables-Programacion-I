#Desarrolle un programa que almacene datos de canciones en formato MP3: Artista,
#Título, Duración (en segundos), Tamaño del fichero (en KB). Un programa debe
#pedir los datos de una canción al usuario y después mostrarlos en pantalla.
#Debe interrumpirse la carga cuando el artista ingresado sea vacío.

album = []

artista = input("Ingrese el nombre del artista: ")
while(artista != ""):
    cancion = {}
    titulo = input("Ingrese el nombre del titulo: ")
    duracion = int(input("Ingrese la duracion en segundos: "))
    tamanio =  int(input("Ingrese el tamaño en Mb: "))

    cancion["artista"] = artista
    cancion["titulo"] = titulo
    cancion["duracion"] = duracion
    cancion["tamanio"] = tamanio

    album.append(cancion)
    artista = input("Ingrese el nombre del artista: ")
    
for cancion in album:
    print("Artista:", cancion["artista"], "Título:", cancion["titulo"], "Duración:", cancion["duracion"], "Tamaño:", cancion["tamanio"])
