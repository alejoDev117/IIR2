# 1. Verifique si está presente "apple"
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Sí, ¡manzana es una fruta!")

# 2. Crear una lista con países y un set con ciudades. Unirlos en un set
paises = ["Colombia", "Perú", "Chile"]
ciudades = {"Medellín", "Lima", "Santiago"}
union = set(paises) | ciudades
print("Unión de países y ciudades:", union)

# 3. Descripción del código
animales_terrestres = set(["Tortuga", "Lobo", "Perro", "Cangrejo"])
print("Terrestres: ", animales_terrestres)
animales_acuaticos = set(["Tiburón", "Pulpo", "Tortuga", "Cangrejo"])
print("Acuáticos: ", animales_acuaticos)
todos_los_animales = animales_terrestres.union(animales_acuaticos)
print("Unión: ", todos_los_animales)

# 4. Recuerde otras colecciones y vaya tomando las diferencias
# (Listas, Tuplas, sets)
lista = [1, 2, 3, 4, 5]
tupla = (4, 5, 6, 7, 8)
conjunto = {7, 8, 9, 10, 11}

# Diferencia entre lista y tupla
dif_lista_tupla = set(lista) - set(tupla)
print("Diferencia entre lista y tupla:", dif_lista_tupla)

# Diferencia entre tupla y conjunto
dif_tupla_conjunto = set(tupla) - conjunto
print("Diferencia entre tupla y conjunto:", dif_tupla_conjunto)

# Diferencia entre conjunto y lista
dif_conjunto_lista = conjunto - set(lista)
print("Diferencia entre conjunto y lista:", dif_conjunto_lista)

# Listas:
frutas = ["manzana", "plátano", "naranja", "manzana", "pera"]
print("Lista de frutas:", frutas)

frutas.append("uva")  # Agregar una fruta al final de la lista
print("Lista después de agregar una fruta:", frutas)

frutas.insert(2, "piña")  # Insertar una fruta en una posición específica
print("Lista después de insertar una fruta:", frutas)

frutas.remove("naranja")  # Eliminar una fruta de la lista
print("Lista después de eliminar una fruta:", frutas)

# Tuplas:
colores = ("rojo", "verde", "azul", "amarillo", "rojo")
print("Tupla de colores:", colores)

apariciones_rojo = colores.count("rojo")  # Contar cuántas veces aparece "rojo"
print("Número de veces que aparece 'rojo':", apariciones_rojo)

indice_azul = colores.index("azul")  # Obtener el índice de "azul"
print("Índice de 'azul':", indice_azul)

# Sets:
letras = {"a", "b", "c", "d", "e", "f", "g"}
print("Conjunto de letras:", letras)

letras.add("h")  # Agregar una nueva letra al conjunto
print("Conjunto después de agregar una letra:", letras)

letras.remove("b")  # Eliminar una letra del conjunto
print("Conjunto después de eliminar una letra:", letras)

otras_letras = {"d", "e", "f", "g", "h", "i", "j"}
diferencia = letras - otras_letras  # Calcular la diferencia entre dos conjuntos
print("Diferencia entre conjuntos:", diferencia)
