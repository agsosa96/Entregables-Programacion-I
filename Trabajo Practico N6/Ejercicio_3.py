#Crear un archivo que se llame “montos.txt”, en el mismo se almacenarán valores
#numéricos. Realizar un proceso que visualice su contenido y, al finalizar,
#muestre el total (sumatoria de los valores) y promedio.

archivo = open("archivos/montos.txt","w")

montos = -1000
while(montos != -1):
    try:
        montos = int(input("Ingrese un monto (Termina con -1): "))
        if(montos != -1):
            archivo.write(str(montos) + "\n")
    except ValueError:
        print("El monto ingresado tiene que ser un numero entero")
        

archivo.close()

try:
    archivo = open("archivos/montos.txt", "r")
    contenido = archivo.read()
    contenidoMontos = contenido.split("\n")

    print(contenidoMontos)

    archivo.close()
except FileNotFoundError:
    print("no se encontro el archivo")
