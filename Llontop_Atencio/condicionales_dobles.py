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
#caso contrario "estudie"
if ( promedio > 11 ):
     print(nombre,", felicidades aprobaste")
else :
    print(nombre,", estudie")
#fin_if


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
#caso contrario "adulto no alcoholico"
if( nro_botellas > 50 ):
    print(nombre_adulto,", adulto alcoholico")
else :
    print(nombre_adulto,", adulto no alcoholico")
#fin_if


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
#mostrar "bienvenido"
#caso contrario "lo sentimos"
if( edad_adolescente > 18 ):
    print(nombre_adolescente,", bienvenido")
else :
    print(nombre_adolescente,", lo sentimos")
#fin_if
