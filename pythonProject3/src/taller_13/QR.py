import os
import qrcode

def crear_codigo_qr(datos, carpeta_destino):
    for nombre, apellido in datos:
        nombre_completo = f"{nombre} {apellido}"
        qr = qrcode.make(nombre_completo)
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        qr.save(os.path.join(carpeta_destino, f"{nombre}_{apellido}_qr.png"))

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        return [linea.strip().split(',') for linea in f]

def main():
    archivo = 'datos.txt'
    hombres = []
    mujeres = []

    for nombre, apellido, _, genero, _, _ in leer_archivo(archivo):
        if genero == 'M':
            hombres.append((nombre, apellido))
        else:
            mujeres.append((nombre, apellido))

    crear_codigo_qr(hombres, os.path.join('miQR', 'hombres'))
    crear_codigo_qr(mujeres, os.path.join('miQR', 'mujeres'))

if __name__ == "__main__":
    main()
