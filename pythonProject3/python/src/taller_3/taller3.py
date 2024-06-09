#Ejericio 1
edad = input("Ingrese su edad\n")

print(f"Tu edad en meses es: {edad * 12}")
#En python es posible multiplicar los string, lo que ocurre es que no se efectua la operacion, si no que se aumentan los caracteres.

edad  = int(input("Ingrese su edad\n"))
print(f"Tu edad en meses es: {edad * 12}")

#Ejercicio 2
valorUnitario = 5000
print("Valor total: " + str(valorUnitario * 12))

#Ejercicio 3
#Casteo
valor = input("Ingrese un valor\n")
print("valor: ",type(valor))
valorInt = int(valor)
print("valor: ",type(valorInt))
valorDecimal = float(valor)
print("valor: ",type(valorDecimal))
cadena = valor + str(valorInt) + str(valorDecimal)
print(cadena)
print("--------------------")
print(f"{valor} {valorInt} {valorDecimal}")

#Ejercicio 4
def tuplaALista(tupla):
    lista = list(tupla)
    return lista
def listATupla(lista):
    tupla = tuple(lista)
    return tupla

listaPaises = ["Colombia","argentina","peru"]
tuplaCiudades = ("Cali","Bogota","Neiva","Manizales")
print("lISTA PAISES: ",type(listaPaises))
print("TUPLA CIUDADES: ",type(tuplaCiudades))
print("TUPLA PAISES:",type(listATupla(listaPaises)))
print("LISTA CIUDADES:",type(tuplaALista(tuplaCiudades)))

