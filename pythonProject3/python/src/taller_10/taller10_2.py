import subprocess

archivo = 'datos.txt'
with open(archivo, 'r') as f:
    for linea in f:
        print(linea.strip())

print("\nListado:")
with open(archivo, 'r') as f:
    for i, linea in enumerate(f, 1):
        nombre, apellido, estatura = linea.strip().split()
        print(f"{i}-{nombre} {apellido} > {estatura}")

nuevo_archivo = 'datos_nuevos.csv'
with open(nuevo_archivo, 'w') as f:
    f.write("Apellido,Nombre,Puntuación,Estatura\n")
    with open(archivo, 'r') as f_datos:
        for linea in f_datos:
            apellido, nombre, estatura = linea.strip().split()
            puntuacion = len(nombre) + len(apellido)
            f.write(f"{apellido},{nombre},{puntuacion},{estatura}\n")

subprocess.Popen(['start', '', nuevo_archivo], shell=True)
