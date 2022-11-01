#Ejercicio 3

signos = {
   'aries':       (( 3, 21), ( 4, 20)),
   'tauro':       (( 4, 21), ( 5, 21)),
   'geminis':     (( 5, 22), ( 6, 21)),
   'cancer':      (( 6, 22), ( 7, 23)),
   'leo':         (( 7, 24), ( 8, 23)),
   'virgo':       (( 8, 24), ( 9, 23)),
   'libra':       (( 9, 24), (10, 23)),
   'escorpio':    ((10, 24), (11, 22)),
   'sagitario':   ((11, 23), (12, 21)),
   'acuario':     (( 1, 21), ( 2, 19)),
   'piscis':      (( 2, 20), ( 3, 20)),
   'capricornio': ((12, 22), ( 1, 20)),
}

def obtenerSigno(fechaNacimiento):
    mes, dia, anio = fechaNacimiento
    fecha = (mes,dia)
    for signo in signos:
        if signos[signo][0]<= fecha and signos[signo][1] >= fecha:
            return signo
    
    return "capricornio"
         
    

#Programa Principal
print(obtenerSigno((2,29,1995))) 
