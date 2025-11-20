# Ejercicio 16 * Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.

numero = int(input("Ingrese un número entre 0 y 99999: "))

if 0 <= numero <= 999999:
    cifras = len(str(numero))
    print(f"El número {numero} tiene {cifras} cifras")
else:
    print("El número ingresado está fuera del rango permitido (0 - 99999)")
5
