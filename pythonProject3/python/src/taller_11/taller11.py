def es_mayor_de_edad(edad):
    return edad >= 18

def contar_mayores_de_80_puntos(puntuacion):
    return puntuacion > 80

archivo = 'archivo.txt'

contador_mayores_de_edad = 0
contador_mas_de_80_puntos = 0
with open(archivo, 'r') as f:
    for linea in f:
        nombre, apellido, edad_str, genero, altura_str, puntaje_str = linea.strip().split(',')
        nombre_apellido = nombre.upper() + " " + apellido.upper()
        edad = int(edad_str)
        altura = int(altura_str) - 2
        puntaje = int(puntaje_str)

        if es_mayor_de_edad(edad):
            contador_mayores_de_edad += 1

        if contar_mayores_de_80_puntos(puntaje):
            contador_mas_de_80_puntos += 1

        print(f"Nombre: {nombre_apellido}, Sexo: {genero}, Edad: {edad}")

print(f"Total de personas mayores de edad: {contador_mayores_de_edad}")
print(f"Total de personas con más de 80 puntos: {contador_mas_de_80_puntos}")
