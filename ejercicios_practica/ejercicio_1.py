# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if numero_1 > numero_2 :
    print(f'{numero_1} es el mayor')
elif numero_1 < numero_2:
    print(f'{numero_2} es el mayor')
else: print("Son iguales")


# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if numero_1 > 0 :
    print(f'{numero_1} es Positivo')
elif numero_1 < 0:
    print(f'{numero_1} es Negativo')
else: print("El número 1 es CERO")

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if (numero_1 > 0 and numero_1 < 100):
    print("El Número 1 está entre 0 y 100")

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
if (numero_1 < 10 or numero_2 > -2):
    print("Se cumple con la condición de que el Numero 1 sea menor a 10 o el Numero 2 mayor a -2")
    # # Imprima en pantalla si se cumple o no la condición