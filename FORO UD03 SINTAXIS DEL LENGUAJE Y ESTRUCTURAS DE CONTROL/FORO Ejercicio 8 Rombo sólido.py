# Ejercicio 8: Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.
# Figura para n=4:

try:
    n = int(input("Introduce n (n >= 1): "))
    if n < 1:
        raise ValueError("n debe ser al menos 1.")
except ValueError as e:
    print("Error:", e)
else:
    # Parte superior (incluye la fila central)
    for i in range(1, n + 1):
        espacios = n - i
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)

    # Parte inferior
    for i in range(n - 1, 0, -1):
        espacios = n - i
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)
