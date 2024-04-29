ciudades = ["Medellín", "Cúcuta"]
paises = ("Colombia", "Perú", "Chile", "Ecuador", "México", "Bolivia", "Perú")

# a) Imprimir la tupla
print("Tupla de países:", paises)

# b) Imprimir la longitud de la tupla
print("Longitud de la tupla:", len(paises))

# c) Imprimir la posición de "Chile"
print("Posición de 'Chile':", paises.index("Chile"))

# d) Cuantas veces está "Perú"
print("Número de veces que está 'Perú':", paises.count("Perú"))

# e) Cuantas veces está "Chile"
print("Número de veces que está 'Chile':", paises.count("Chile"))

# f) Adicionar el país "Argentina"
paises += ("Argentina",)

# g) Imprimir los 3 primeros elementos
print("Los 3 primeros elementos:", paises[:3])

# h) Imprimir los últimos 3 elementos
print("Los últimos 3 elementos:", paises[-3:])

# i) Imprimir los elementos del 2 al 5
print("Elementos del 2 al 5:", paises[1:5])

# j) Unir la lista ciudades con la tupla países
lista_unida = ciudades + list(paises)
print("Lista unida:", lista_unida)
