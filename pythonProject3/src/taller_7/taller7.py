#Ejercicio 1
a = 33
b = 200
if b > a:
    print("b es mas grande que a\n")

print(a) if a > b else print(b)

#Ejercicio 2
def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado."""
    return lado ** 2

def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2

# Solicitar al usuario que ingrese la figura
figura = input("¿Qué figura desea calcular? (cuadrado/triángulo): ")

if figura.lower() == "cuadrado":
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = calcular_area_cuadrado(lado)
    print("El área del cuadrado es:", area)
elif figura.lower() == "triángulo":
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = calcular_area_triangulo(base, altura)
    print("El área del triángulo es:", area)
else:
    print("Figura no válida. Por favor, elija 'cuadrado' o 'triángulo'.")

import random

def jugar_adivinanza(intentos, numero_secreto):
    """Juego de adivinanzas."""
    print("Bienvenido al juego de adivinanzas!")
    print(f"Tienes {intentos} intentos para adivinar el número secreto.")

    for intento in range(1, intentos + 1):
        intento_usuario = int(input("Intento #{}: Ingresa tu número: ".format(intento)))
        if intento_usuario == numero_secreto:
            print("¡Felicidades! ¡Has adivinado el número secreto!")
            return
        elif intento_usuario < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

    print("Lo siento, has agotado tus intentos. El número secreto era:", numero_secreto)

# Generar un número aleatorio como número secreto
numero_secreto = random.randint(1, 100)
intentos = 5  # Número de intentos que tiene el jugador

# Jugar la adivinanza
jugar_adivinanza(intentos, numero_secreto)

def asignar_calificacion(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"

nota = float(input("Ingrese la nota del estudiante: "))
calificacion = asignar_calificacion(nota)
print("La calificación del estudiante es:", calificacion)
