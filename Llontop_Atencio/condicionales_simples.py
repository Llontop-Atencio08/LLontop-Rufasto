#programa alumno aprobado
import os
#declaracion
nombre=""
promedio=0.0

#Input via os
nombre=os.sys.argv[1]
promedio=float(os.sys.argv[2])

#procesing
#si el alumno supera a 11
#mostrar "felicidades aprobaste"
if(promedio>11):
     print(nombre,"felicidades aprobaste")


#Ejercicio2
#programa de adulto alcoholico
import os
#declaracion
nombre_adulto=""
nro_botellas=0

#Input via os
nombre_adulto=os.sys.argv[1]
nro_botellas=int(os.sys.argv[2])

#procesing
#si el nro de botellas supera a 50
#mostrar "adulto alcoholico"
if(nro_botellas>50):
    print(nombre_adulto,"adulto alcoholico")


#Ejercicio3
#programa de adolescente para ingreso a discoteca
import os
#declaracion
nombre_adolescente=""
nombre_discoteca=""
edad_adolescente=0

#Input via os
nombre_adolescente=os.sys.argv[1]
nombre_discoteca=os.sys.argv[2]
edad_adolescente=int(os.sys.argv[3])

#procesing
#si la edad supera a los 18 anios
#mostrar "adulto mayor de edad"
if(edad_adolescente>18):
    print(nombre_adolescente,"bienvenido")
