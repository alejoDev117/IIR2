import os

def calcular_imc(peso, altura):
    return peso / ((altura / 100) ** 2)

def crear_archivo(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as f:
        for nombre, imc in datos:
            f.write(f"{nombre}: {imc}\n")

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        return [linea.strip().split(',') for linea in f]

def main():
    archivo = 'datos.txt'
    personas_con_imc_mayor_20 = []
    mujeres_con_imc = []

    for nombre, apellido, edad_str, genero, altura_str, peso_str in leer_archivo(archivo):
        edad = int(edad_str)
        altura = int(altura_str)
        peso = int(peso_str)
        imc = calcular_imc(peso, altura)

        if imc > 20:
            personas_con_imc_mayor_20.append((nombre, imc))

        if genero == 'F':
            mujeres_con_imc.append((nombre, imc))

    archivo_mayor_20 = 'imc_mayor_20.txt'
    crear_archivo(archivo_mayor_20, personas_con_imc_mayor_20)

    archivo_mujeres = 'imc_mujeres.txt'
    crear_archivo(archivo_mujeres, mujeres_con_imc)

    print(f"Total de personas con IMC mayor a 20: {len(personas_con_imc_mayor_20)}")
    print(f"Ruta del archivo IMC mayor a 20: {os.getcwd()}\\{archivo_mayor_20}")
    print(f"Ruta de los archivos creados: {os.getcwd()}")

if __name__ == "__main__":
    main()
