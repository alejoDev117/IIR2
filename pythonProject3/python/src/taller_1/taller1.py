#Ejercicio 1
import math

pais = "Colombia"
nombre = input("Ingrese su nombre\n")
apellido = input("Ingrese su primer apellido\n")
edad = int(input("Ingrese su edad(en años)\n"))

print("--------------")
print(type(pais))
print(type(nombre))
print(type(apellido))
print(type(edad))

print("Hola como estas: ",nombre+apellido+"Bienvenido a: ",pais)

#Ejercicio 2

pi = math.pi
print(pi)
print(type(pi))

nombreAlumno = input("Ingrese el nombre del estudiante\n")
nombreAcudiente = input("Ingrese el nombre del acudiente\n")

print(nombreAcudiente, "Es el acudiente de ", nombreAlumno.upper())
print(nombreAcudiente.upper(), "Es el acudiente de ", nombreAlumno.upper())

print(nombreAcudiente.lower(), "Es el acudiente de ", nombreAlumno.lower())
print(f"Resultados del { nombreAlumno } los representa: { nombreAcudiente }")
print("el tipo de dato del alumno es: ", type(nombreAlumno) )

#Ejercicio 3
year = 2016
evento = "Referendum"
print(f"Resultados del {evento} {year}")

#Area circulo
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2

print(f"El área del círculo con radio {radio} es: {area}")

