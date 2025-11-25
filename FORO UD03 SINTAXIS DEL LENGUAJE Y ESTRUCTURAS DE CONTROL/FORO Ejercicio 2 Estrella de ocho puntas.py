# *Ejercicio 2: Estrella de ocho puntas.
# Enunciado: Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impor n x n (ej. 9x9)
# Figura para n=9:
try:
    n = int(input("Introduce el tamaño (impar): "))
    if n <= 0 or n % 2 == 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número impar mayor que cero")
else:
    centro = n // 2
    for i in range(n):
        fila = ""
        for j in range(n):
            # Dibujamos fila central, columna central y diagonales
            if i == centro or j == centro or i == j or i + j == n - 1:
                fila += "*"
            else:
                fila += " "
        print(fila)
