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



#Ejercicio4
#programa de consultora compulsiva
import os
#declaracion
nombre_consultora=""
total_de_la_compra=0.0

#Input via os
nombre_consultora=os.sys.argv[1]
total_de_la_compra=float(os.sys.argv[2])

#procesing
#si la compra supera los 600 soles
#mostrar "consultora compulsiva"
#caso contrario "no eres consultora compulsiva"
if( total_de_la_compra > 600 ):
    print(nombre_consultora,", compradora compulsiva")
else :
    print(nombre_consultora,", no eres compradora compulsiva")


#Ejercicio5
#programa de empleado compulsivo
import os
#declaracion
nombre_empleado=""
monto_total=0.0

#Input via os
nombre_empleado=os.sys.argv[1]
monto_total=float(os.sys.argv[2])

#procesing
#si el empleado supera los 2000
#mostrar "empleado compulsivo"
#caso contrario "usted no es un empleado compulsivo"
if( monto_total > 2000 ):
    print(nombre_empleado,", empleado compulsivo")
else :
    print(nombre_empleado,", usted no es un empleado compulsivo")



#Ejercicio5
#programa de empleado compulsivo
import os
#declaracion
nombre_empleado=""
monto_total=0.0

#Input via os
nombre_empleado=os.sys.argv[1]
monto_total=float(os.sys.argv[2])

#procesing
#si el empleado supera los 2000
#mostrar "empleado compulsivo"
#caso contrario "usted no es un empleado compulsivo"
if( monto_total > 2000 ):
    print(nombre_empleado,", empleado compulsivo")
else :
    print(nombre_empleado,", usted no es un empleado compulsivo")
#fin_if


#Ejercicio6
#programa de exceso de alumnos
import os
#declaracion
nombre_colegio=""
cantidad_total=0

#Input via os
nombre_colegio=os.sys.argv[1]
cantidad_total=int(os.sys.argv[2])

#procesing
#si la cantidad de alumnos supera los 300
#mostrar "lo sentimos, exceso de alumnos"
#caso contrario "felicidades alcanzo vacante"
if( cantidad_total > 300 ):
    print(nombre_colegio,", lo sentimos, exceso de alumnos")
else :
    print(nombre_colegio,", felicidades alcanzo vacante")
#fin_if
