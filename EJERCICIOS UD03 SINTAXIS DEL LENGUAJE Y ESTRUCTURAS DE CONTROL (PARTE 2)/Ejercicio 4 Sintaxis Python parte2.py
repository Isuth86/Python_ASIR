# Ejercicio 4: Programa que muestre los números desde el 1 hasta un número N que se introducirá por
# teclado.

try:
    N = int(input("Introduce un número positivo: "))
    if N <= 0:
        raise ValueError("El número debe ser mayor que cero.")
except ValueError as e:
    print("Error:", e)
else:
    for i in range(1, N + 1):
        print(i)
