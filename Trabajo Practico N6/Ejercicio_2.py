#En base al primer punto, luego de generar la carga de las frases, visualizar
#el archivo cargado.

try:
    contenido = open("archivos/frases.txt","r")
    frasesContenidas = contenido.read()

    print(frasesContenidas)
    contenido.close()
except FileNotFoundError:
    print("El archivo no existe")
