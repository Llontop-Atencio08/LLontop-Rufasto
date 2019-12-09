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
if ( total >=30 and total <=39):
    print("no tiene problemas con el alcohol")


#Ejercicio4
#programa de consultora compulsiva
import os
#declaracion
nombre_consultora,mes1,mes2,mes3="",0.0,0.0,0.0

#Input via os
nombre_consultora=os.sys.argv[1]
mes1=float(os.sys.argv[2])
mes2=float(os.sys.argv[3])
mes3=float(os.sys.argv[4])

#procesing
total=float(round(mes1+mes2+mes3))
#Condicion multiple
#si la suma total =>1000 y 1500 (usted es una consultora compulsiva)
if( total >= 1000 and total <=1500):
    print("usted es una compradora compulsiva")
#si la suma total => 500 y 999 (usted no es compradora impulsiva)
if ( total >= 500 and total <=999):
    print("usted no es compradora compulsiva")


#Ejercicio5
#programa de empleado compulsivo
import os
#declaracion
nombre_empleado,mes1,mes2,mes3="",0.0,0.0,0.0

#Input via os
nombre_empleado=os.sys.argv[1]
mesl=float(os.sys.argv[2])
mes2=float(os.sys.argv[3])
mes3=float(os.sys.argv[4])

#procesing
total=float(round(mesl+mes2+mes3))
#Condicion multiple
#si la suma total =>7000 y 7500 (usted es un empleado compulsivo)
if(total >= 7000 and total <=7500 ):
    print("usted es un empleado compulsivo")
#si la suma total =>5000 y 6999 (usted no es empleado compulsivo)
if ( total >= 5000 and total <=6999 ):)
    print(" usted no es un empleado compulsivo")
