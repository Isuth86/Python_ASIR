# Ejercicio 9: Imprime un cuadrado de lado n con borde y diagonales en asteriscos, y un cuadro hueco centrado dentro.
# Figura para n=9:

try:
    n = int(input("Introduce el tamaño del cuadrado (n >= 2): "))
    if n < 2:
        raise ValueError("n debe ser al menos 2.")
except ValueError as e:
    print("Error:", e)
else:
    c = n // 2  # centro (solo relevante cuando n es impar)
    for i in range(n):
        fila = []
        for j in range(n):
            borde = (i == 0 or i == n - 1 or j == 0 or j == n - 1)
            diag = (i == j or i + j == n - 1)
            centro_cruce = (i == c and j == c) and (n % 2 == 1)
            if borde or (diag and not centro_cruce):
                fila.append("*")
            else:
                fila.append(" ")
        print("".join(fila))
