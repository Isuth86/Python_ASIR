# Ejercicio 12: Crea una aplicación que dibuje una escalera de números, siendo cada línea un número.
# Nosotros le pasamos la altura por teclado.
try:
    altura = int(input("Introduce la altura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un entero mayor que cero.")
else:
    for i in range(1, altura + 1):
        print(str(i) * i)
