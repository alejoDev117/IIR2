
#Ejercicio 1
numero1 = int(input("Ingrese el primer numero\n"))
numero2 = float(input("Ingrese un numero decimal\n"))

print(f"La suma de sus dos numeros es: {numero1 + numero2}")
print(f"La resta de sus dos numeros es: {numero1 - numero2}")
print(f"La multiplicacion de sus dos numeros es: {numero1 * numero2}")
print(f"La division de sus dos numeros es: {numero1 / numero2}")
#Ejercicio 2

#Area del triangulo
alturaTriangulo = float(input("Ingrese la altura del triangulo\n"))
baseTriangullo = float(input("Ingrese la base del triangulo\n"))
areaTriangulo = (baseTriangullo * alturaTriangulo) / 2
print("El area del trangulo es :"+ str(areaTriangulo))
#Area del cuadrado
lado = float(input("Ingrese el lado del cuadrado\n"))
print(f"El area del cuadrado: {lado*lado}")
#Area rectangulo usando shapely
a = float(input("Ingrese la base del rectangulo\n"))
b = float(input("Ingrese la altura del rectangulo\n"))
rectangulo = a * b
print(rectangulo)
#Area del circulo
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
print(f"El área del círculo con radio {radio} es: {area}")



