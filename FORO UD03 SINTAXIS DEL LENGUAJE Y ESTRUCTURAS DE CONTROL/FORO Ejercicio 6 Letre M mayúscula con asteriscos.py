# Ejercicio 6: Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n. Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.
# Figura para n=7:
try:
    n = int(input("Introduce un tamaño impar (n >= 3): "))
    if n < 3 or n % 2 == 0:
        raise ValueError("n debe ser impar y mayor o igual que 3.")
except ValueError as e:
    print("Error:", e)
else:
    c = n // 2  # fila central
    for i in range(n):
        fila = []
        for j in range(n):
            # Verticales de la M
            if j == 0 or j == n - 1:
                fila.append("*")
            # Diagonales internas (solo hasta la mitad)
            elif i <= c and (j == i or j == n - 1 - i):
                fila.append("*")
            else:
                fila.append(" ")
        print("".join(fila))
