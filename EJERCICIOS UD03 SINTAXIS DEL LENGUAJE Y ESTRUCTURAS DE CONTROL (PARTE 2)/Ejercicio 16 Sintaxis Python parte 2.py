# Ejercicio 16: Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.
try:
    print("Introduce las notas (0 a 10). Termina con -1:")
    hubo_diez = False

    while True:
        nota = int(input("Nota: "))

        if nota == -1:   # condición de fin
            break
        elif nota < 0 or nota > 10:
            print("Error: la nota debe estar entre 0 y 10")
        else:
            if nota == 10:
                hubo_diez = True

    if hubo_diez:
        print("Sí hubo alguna nota con valor 10.")
    else:
        print("No hubo ninguna nota con valor 10.")

except ValueError:
    print("Error: Debes introducir números enteros.")
