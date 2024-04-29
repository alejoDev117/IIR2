#Ejercicio 1
votos = 42_572_654
noVotos = 12_333_300
print(type(votos))
#variables
print("votantes: {} no votantes : {}\n".format(votos, noVotos))
perc = votos / (votos + noVotos)
print('{:-10} YES votes {:2.3%}'.format(votos, perc))
#Mas ejemplos
precio = 24.99
cantidad = 3
total = precio * cantidad
print("Precio: ${:.2f} Cantidad: {} Total: ${:.2f}".format(precio, cantidad, total))

nombre = "Juan"
apellido = "Pérez"
print("Nombre: {:<10} Apellido: {:>10}".format(nombre, apellido))

print("Los {0} saltan sobre {1}".format("gatos", "perros"))

numero = 255
print("Número en hexadecimal: {:X}".format(numero))

for i in range(1, 11):
    for j in range(1, 11):
        print("{:2d} x {:2d} = {:2d}".format(i, j, i*j))
    print("-" * 12)

personas = [("Juan", 30), ("María", 25), ("Pedro", 40)]
print("Nombre    Edad")
print("-" * 15)
for nombre, edad in personas:
    print("{:<10} {:>5}".format(nombre, edad))


numero = 0.5
# Se formatea el valor como un porcentaje
print("El valor es: {:2.2%}".format(numero))
area = 1973.9208802178716
print('El area es: {:,.2f}'.format(area))
#separadores de 1000 y 2 decimales
print('El area es: {:,.2f}'.format(area))
#reemplaza la coma (,) por asterisco (*)
print('El area es: {:,.2f}'.format(area).replace(",", "*"))
#El area es: 1.973,92