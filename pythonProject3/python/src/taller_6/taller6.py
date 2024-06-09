#Ejercicio 1
paises = ["Estados Unidos", "Francia", "Japón", "Brasil", "Australia", "India"]
ciudades = ["Nueva York", "París", "Tokio", "Río de Janeiro", "Sídney"]

print("Longitud de paises: ",len(paises))
print("Longitud de ciudades: ",len(ciudades))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))

#Ejercicio 2
print(paises[:2])
print(ciudades[:2])
print(paises[3])
print(ciudades[3])


#Ejercicio 3
paises.sort()
ciudades.sort()
print("Países ordenados:", paises)
print("Ciudades ordenadas:", ciudades)

lista_completa = paises + ciudades
print("Lista completa:", lista_completa)

paises.insert(1, "Canadá")
ciudades.insert(1, "Londres")
print("Países con un elemento insertado:", paises)
print("Ciudades con un elemento insertado:", ciudades)

paises.append("China")
ciudades.append("Berlín")
print("Países con un elemento adicionado:", paises)
print("Ciudades con un elemento adicionado:", ciudades)

paises.remove(paises[0])
ciudades.remove(ciudades[0])
print("Países con el primer elemento eliminado:", paises)
print("Ciudades con el primer elemento eliminado:", ciudades)

# append() - Agrega un elemento al final de la lista
paises.append("China")
ciudades.append("Berlín")

# clear() - Elimina todos los elementos de la lista
paises.clear()
ciudades.clear()

# copy() - Devuelve una copia de la lista
paises = ["Estados Unidos", "Francia", "Japón", "Brasil", "Australia", "India"]
ciudades = ["Nueva York", "París", "Tokio", "Río de Janeiro", "Sídney"]
paises_copia = paises.copy()
ciudades_copia = ciudades.copy()

# count() - Devuelve el número de elementos con el valor especificado
num_francia = paises.count("Francia")
print("Número de veces que aparece 'Francia' en la lista de países:", num_francia)

# extend() - Añade los elementos de una lista (o cualquier iterable) al final de la lista actual
otros_paises = ["Canadá", "México", "Alemania"]
paises.extend(otros_paises)

# index() - Devuelve el índice del primer elemento con el valor especificado
indice_rio = ciudades.index("Río de Janeiro")
print("El índice de 'Río de Janeiro' en la lista de ciudades es:", indice_rio)

# insert() - Agrega un elemento en la posición especificada
ciudades.insert(2, "Londres")

# pop() - Elimina el elemento en la posición especificada
elemento_eliminado = paises.pop(3)
print("Elemento eliminado de la lista de países:", elemento_eliminado)

# remove() - Elimina el elemento con el valor especificado
ciudades.remove("Nueva York")

# Imprimir los resultados
print("Lista de países:", paises)
print("Lista de ciudades:", ciudades)
print("Copia de la lista de países:", paises_copia)
print("Copia de la lista de ciudades:", ciudades_copia)

