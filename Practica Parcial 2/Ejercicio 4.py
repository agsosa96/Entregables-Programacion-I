def codigoLibro(cadena):
    for IDLibros in libros:
        if(libros[IDLibros] == cadena):
            return IDLibros
        
    return -1

def datosLibro(algo):
    for IDLibros in libroDatos:
        if(IDLibros == algo):
            autor, editorial, fechaPublicacion = libroDatos[IDLibros].values()
            return  autor, editorial, fechaPublicacion


libros = {
    1001: "La uruguaya",
    1003: "Ser feliz era esto"
}

libroDatos = {
    1001 : {
        "autor":"Pedro Mairal",
        "editorial":"Alfaguara",
        "fechaPublicacion": 2021
    },
    1003 : {
        "autor":"Eduardo Sacheri",
        "editorial":"Planeta",
        "fechaPublicacion": 2018
    }    
}

#Programa Principal
bandera = -100
while(bandera != 0):
    titulo = input('Ingrese titulo del libro: ')
    if(codigoLibro(titulo) != -1):
        print ("Código de libro: ", codigoLibro(titulo))
        bandera = 0
    
    
autor, editorial, fechaPublicacion = datosLibro(codigoLibro(titulo))
print (f"Autor:  {autor} \nEditorial: {editorial} \nFecha de publicación: {fechaPublicacion}")

