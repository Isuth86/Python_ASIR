# * Ejercicio 13
# Crea una aplicación que dibuje una escalero de números, siendo cada línea números empezando
try:
    altura = int(input("Introduce la altura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("ERROR: Debes introducir un número mayor que cero")
else:
    # Construimos la escalera de números.
    for i in range(1, altura + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
