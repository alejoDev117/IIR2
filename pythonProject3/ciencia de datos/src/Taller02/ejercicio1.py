import os
import shutil

try:
    file = open("IIR2.txt","w")
    file.write("Id  mes  dias_cotizados  porcentaje  valorbase  aporte\n")
    id = 1
    for i in range(3):
       texto = input("Ingrese mes, dias cotizados, porcentaje y valor base recuerde hacerlo con espacios\n")
       datosNumericos = texto.split()
       file.write(str(id) +"     "+ texto +"      "+ str((float(datosNumericos[1]) * float(datosNumericos[2])/100)/float(datosNumericos[3]))+"\n")
       id += 1

finally:
    file.close()
