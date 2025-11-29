# *Ejercicio 3: Pirámide con huecos internos (estructura tipo "reja").
# Enunciado: Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.
# Figura para n=6:
try:
    n = int(input("Introduce la altura de la pirámide: "))
    if n <= 0:
        raise ValueError("La altura debe ser positiva.")
except ValueError as e:
    print("Error:", e)
else:
    for i in range(1, n + 1):
        # espacios iniciales para centrar
        espacios = " " * (n - i)

        if i == 1:
            # primera fila: solo un asterisco
            fila = "*"
        elif i == n:
            # última fila: todo asteriscos
            fila = "*" * (2 * n - 1)
        elif i % 2 == 0:
            # filas pares: alternancia de asteriscos y espacios
            fila = "* " * i
            fila = fila.strip()
        else:
            # filas impares intermedias: extremos con huecos dentro
            fila = "*" + " " * (2 * i - 3) + "*"

        print(espacios + fila)
