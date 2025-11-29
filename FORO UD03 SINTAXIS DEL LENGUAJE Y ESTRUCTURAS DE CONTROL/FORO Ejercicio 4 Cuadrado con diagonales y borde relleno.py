# Ejercicio 4: Imprime un cuadrado de lado n con bordes de asteriscos y las dos diagnonales marcadas, dejando espacios en el esto.
# Figura para n=7:
try:
    n = int(input("Introduce el tamaño del cuadrado (n >= 2): "))
    if n < 2:
        raise ValueError("El tamaño debe ser al menos 2.")
except ValueError as e:
    print("Error:", e)
else:
    for i in range(n):
        if i == 0 or i == n - 1:
            # primera y última fila: todo asteriscos
            print("*" * n)
        else:
            fila = ""
            # columna interior “zigzag”: 1 + min(i, n-1-i)
            c = 1 + min(i, n - 1 - i)
            for j in range(n):
                if j == 0 or j == n - 1 or j == c:
                    fila += "*"
                else:
                    fila += " "
            print(fila)
