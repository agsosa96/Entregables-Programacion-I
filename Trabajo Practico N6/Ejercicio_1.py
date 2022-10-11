#Crea un programa que vaya leyendo las frases que el usuario teclea y las guarde
#en un fichero de texto llamado “frases.txt”. Terminará cuando la frase
#introducida sea "fin" (esa frase no deberá guardarse en el fichero).

archivo = open("archivos/frases.txt","w")

frase = ""

while(frase != "fin"):
    frase = input("Ingrese una frase: ")
    if(frase != "fin"):
        archivo.write(frase + "\n")


archivo.close()
    
