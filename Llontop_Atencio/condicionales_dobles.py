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
     print(nombre,"felicidades aprobaste")
else :
    print(nombre,"estudie")
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
    print(nombre_adulto,"adulto alcoholico")
else :
    print(nombre_adulto,"adulto no alcoholico")
#fin_if
