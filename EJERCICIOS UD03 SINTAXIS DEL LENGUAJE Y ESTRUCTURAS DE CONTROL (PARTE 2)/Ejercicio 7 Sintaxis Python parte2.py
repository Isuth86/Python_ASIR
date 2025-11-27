# Ejercicio 7: Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún número negativo o no.

try:
    hubo_negativo = False

    print("Introduce 100 números (no nulos):")
    for i in range(1, 101):
        numero = int(input(f"Número {i}: "))
        if numero == 0:
            raise ValueError("No se permiten ceros.")
        elif numero < 0:
            hubo_negativo = True

    # Resultado final
    if hubo_negativo:
        print("Sí se ha leído al menos un número negativo.")
    else:
        print("No se ha leído ningún número negativo.")

except ValueError as e:
    print("Error:", e)
