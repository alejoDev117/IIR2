#Manejo de ficheros
#Escritura
escritura = open("ficheros.txt","w")
escritura.write(input("Ingresa el texto que quieres en el archivo de texto\n"))
escritura.close()
#Lectura
lectura = open("ficheros.txt","r")
fichero = lectura.read()
print(fichero)
dato = lectura.read(5)
print(dato)
linea = lectura.readline()
print(linea)
lectura.close()

f = open("origen.txt")
g = open("destino.txt","w")
linea = f.readline()
while linea != "":
   g.write(linea)
   linea = f.readline()
g.close()
f.close()