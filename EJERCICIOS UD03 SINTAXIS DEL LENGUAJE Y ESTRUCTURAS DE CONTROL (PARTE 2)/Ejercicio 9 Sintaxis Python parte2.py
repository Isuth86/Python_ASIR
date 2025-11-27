# Ejercicio 9: Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
# muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.
try:
    print("Introduce números (termina con 0):")
    hubo_negativo = False
    positivos = 0
    negativos = 0

    while True:
        numero = int(input("Número: "))

        if numero == 0:   # condición de fin
            break
        elif numero > 0:
            positivos += 1
        else:  # número < 0
            negativos += 1
            hubo_negativo = True

    # Resultados
    if hubo_negativo:
        print("Sí se ha leído al menos un número negativo.")
    else:
        print("No se ha leído ningún número negativo.")

    print("Cantidad de números positivos:", positivos)
    print("Cantidad de números negativos:", negativos)

except ValueError:
    print("Error: Debes introducir números enteros.")
