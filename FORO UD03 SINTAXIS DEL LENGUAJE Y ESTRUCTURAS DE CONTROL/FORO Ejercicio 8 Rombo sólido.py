# Ejercicio 8: Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.
# Figura para n=4:
try:
    n = int(input("Introduce n (n >= 1): "))
    if n < 1:
        raise ValueError("n debe ser al menos 1.")
except ValueError as e:
    print("Error:", e)
else:
    altura = 2 * n - 1
    for i in range(1, altura + 1):
        # distancia a la fila central
        d = abs(n - i)
        espacios = d
        asteriscos = 2 * (n - d) - 1
        print(" " * espacios + "*" * asteriscos)
