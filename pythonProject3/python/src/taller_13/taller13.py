import os

nombre_carpeta_padre = "miQR"
os.mkdir(nombre_carpeta_padre)

os.mkdir(os.path.join(nombre_carpeta_padre, "hombres"))
os.mkdir(os.path.join(nombre_carpeta_padre, "mujeres"))
