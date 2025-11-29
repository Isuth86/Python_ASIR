# Ejercicio 18/11/2025 - Triángulo con 4.
n = 5  # altura fija

for i in range(n):
    if i == 0:
        print("4")
    elif i == n - 1:
        print("4 " * n)
    else:
        espacios = " " * (2 * i - 1)
        print("4" + espacios + "4")
