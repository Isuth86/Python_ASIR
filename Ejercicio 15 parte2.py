# * Ejercicio 15
# Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos la altura de la pirámide por teclado.
try:
    altura = int(input("Introduce la altura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número mayor que cero")
else:

    for i in range(altura, 0, -1):
        espacios = altura - i
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)
