# Ejercicio 5: Imprime una cruz en una matriz de tamaño n x n con puntos en el borde, asteriscos en las líneas vertical y horizontal centrales, y espacios en el resto.
# Figura para n=7:
try:
    n = int(input("Introduce el tamaño de la matriz (n impar >= 3): "))
    if n < 3 or n % 2 == 0:
        raise ValueError("n debe ser un número impar mayor o igual que 3.")
except ValueError as e:
    print("Error:", e)
else:
    c = n // 2  # índice central
    for i in range(n):
        fila = []
        for j in range(n):
            # Bordes con puntos
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                fila.append(".")
            # Fila central completa con asteriscos
            elif i == c:
                fila.append("*")
            # Resto de filas: patrón por paridad (rejilla)
            elif (i % 2) == (j % 2):
                fila.append("*")
            else:
                fila.append(".")  # aquí estaban faltando puntos
        print(" ".join(fila))
