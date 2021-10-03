# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2 : 
    print("La primera palabra esta después de la segunda en el abcedario")
elif texto_1 < texto_2:
    print("La primera palabra esta antes de la segunda en el abcedario")
else: print("Las palabras son iguales")
# Compare cual de las dos palabras tiene mayor
# cantidad de letras
if len(texto_1)>len(texto_2):
    print(f"La primera palabra es {texto_1} y es más larga que la segunda")
elif len(texto_1)>len(texto_2):
    print(f"La primera palabra es {texto_1} y es más corta que la segunda")
else: print ("La longitud de las palabras es la misma")

# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
if texto_1[0] > texto_2[0]:
    print("La primera letra de la primera palabra es mayor que la de la segunda")
# Imprima en pantalla según corresponda


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print("Las variables Copia_Texto_1 y Texto_1 son iguales")

if copia_texto_1 != texto_2:
    print("Los textos son distintos")
    