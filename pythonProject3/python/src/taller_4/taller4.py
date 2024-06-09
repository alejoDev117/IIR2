texto = """
Comentario del código o notas explicativas sobre qué hace alguna sección del 
código, son útiles para llevar el control del programa y para minimizar esfuerzos de 
mantenimiento de código. No tienen implicación en la ejecución del programa.

"""
print(texto)

stringAProbar = "Colombia Factor X"
print(stringAProbar)
print(stringAProbar.lower())#Coloca todo en minuscula
print(stringAProbar.upper())#Coloca todo en mayuscula
print(stringAProbar.title())#Coloca solo las primeras letras en mayuscula similar al metodo capiatalize
print(stringAProbar[0])#Devuelve el primer elemento C
print(stringAProbar[2])#Devuelve el tercer elemento l
print(stringAProbar[:2])#Devuevle desde el primer elemento hasta el tercer elemento sin incluirlo
print(stringAProbar[-1])#Devuelve el ultimo elemento X
print(stringAProbar[-2])#Devuelve el penultimo elemento espacio
print(stringAProbar[-3])#Devuelve el tranantepenultimo elemento r

cadena = "IIR2- Tech for all"
print(len(cadena))#Da la longitud de la cadena
print(cadena.capitalize())#Da la cadena con las primeras letras en mayuscula

txt = "Hola bienvenido a IIR2 - IA"
x = txt.find("welcome")#Sirve para buscar un string o palabra en especifico en una cadena de texto
print(x)

txt = "34800"
x = txt.isdigit() #Determina si un String es un valor numerico
print(x)

txt = "Colombia sigue adelante con IIR2"
x = txt.replace("Colombia", "IA")
print(x)
txt = "Colombia sigue adelante con IIR2"
x = txt.replace("IIR2", "IA")
print(x)
#Busca y reemplaza partes especificas del texto
import re
texto = """
El fútbol es un deporte muy popular en España. La selección
española ha ganado la Copa del Mundo en 2010 y ha tenido
grandes jugadores como Xavi, Iniesta y Sergio Ramos.
"""
# Búsqueda de palabras que empiezan con la letra 'e' o 'E'
patron_inicio_e = r'\b[Ee]\w+'
palabras_inicio_e = re.findall(patron_inicio_e, texto)

# Búsqueda de palabras que contienen 'españa' o 'España'
patron_espana = r'\b[Ee]spaña?\w*'
palabras_espana = re.findall(patron_espana, texto)

# Sustitución de 'España' por 'la España'
texto_modificado = re.sub(r'\b(España)\b', r'la \1', texto)

# Imprimir resultados
print("Palabras que empiezan con 'e' o 'E':", palabras_inicio_e)
print("Palabras que contienen 'España' o 'españa':", palabras_espana)
print("Texto modificado:", texto_modificado)

