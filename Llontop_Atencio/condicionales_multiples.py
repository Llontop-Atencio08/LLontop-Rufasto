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
