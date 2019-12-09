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

