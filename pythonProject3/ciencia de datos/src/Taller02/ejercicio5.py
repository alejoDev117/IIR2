import os

ruta_actual = os.getcwd()

carpeta_principal = "IIR2Colombia"

subcarpetas = ["ds", "scripts", "IA"]

ruta_principal = os.path.join(ruta_actual, carpeta_principal)

os.mkdir(ruta_principal)

os.chdir(ruta_principal)
nueva_ruta_actual = os.getcwd()

for subcarpeta in subcarpetas:
    ruta_subcarpeta = os.path.join(nueva_ruta_actual, subcarpeta)
    os.mkdir(ruta_subcarpeta)
