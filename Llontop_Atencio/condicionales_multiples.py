# Programa para calcular 3 notas de lep2
import os

# Declaracion de variables
n1,n2,n3,prom=0,0,0,0

# INPUT VIA OS
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])

# PROCESSING
prom=int(round((n1+n2+n3)/3,0))

# Condicion multiple
# Si el prom => 55 y 60 (Very Good)
if ( prom >=55 and prom <=60 ):
    print("Very Good!")
# Si el prom 50 y 54 (Good)
if ( prom >= 60 and prom <= 54):
    print("Good!")

#Ejercicio2
#programa alumno aprobado
import os
#declaracion
nombre,nota1,nota2,nota3,nota4,promedio="",0,0,0,0,0

#Input via os
nombre=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])
nota4=int(os.sys.argv[5])

#procesing
prom=int(round((nota1+nota2+nota3+nota4)/4.0))
#Condicion multiple
#si el promedio => 75 y 80 (felicitaciones!)
if ( promedio >=75 and promedio <=80 ):
     print("felicitaciones!")
#si el promedio 70 y 74 (muy bien)
if ( promedio >= 70 and promedio <=74):
    prin("muy bien")


#Ejercicio3
#programa de adulto alcoholico
import os
#declaracion
nombre_adulto,botella1,botella2,botella3="",0,0,0

#Input via os
nombre_adulto=os.sys.argv[1]
botella1=int(os.sys.argv[2])
botella2=int(os.sys.argv[3])
botella3=int(os.sys.argv[4])

#procesing
total=int(round(botella1+botella2+botella3))
#Condicion multiple
#si la suma total => 40 y 50 (usted tiene problemas con el alcohol)
if( total >= 40 and total <=50 ):
    print("usted tiene problemas con el alcohol")
#si la suma total =>30 y 39 (no tiene problemas con el alcohol)
if ( promedio >=30 and total <=39):
    print("no tiene problemas con el alcohol")
