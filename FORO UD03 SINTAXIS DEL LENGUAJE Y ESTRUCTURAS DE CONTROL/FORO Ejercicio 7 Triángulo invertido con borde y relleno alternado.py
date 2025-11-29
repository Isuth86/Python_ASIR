# Ejercicio 7: Imprime un triángulo invertido de altura n con asteriscos en el borde, y líneas internas de relleno alternadas entre espacios y asteriscos.
# Figura para n=6:
try:
    n = int(input("Introduce la altura del triángulo (n >= 2): "))
    if n < 2:
        raise ValueError("La altura debe ser al menos 2.")
except ValueError as e:
    print("Error:", e)
else:
    for i in range(n):
        # número de espacios iniciales para centrar
        espacios = " " * i
        # ancho de la fila actual
        ancho = 2 * (n - i) - 1

        if i == 0:
            # primera fila: todo asteriscos
            fila = "*" * ancho
        elif i == n - 1:
            # última fila: solo un asterisco
            fila = "*"
        else:
            # bordes con asteriscos
            if i % 2 == 0:
                # filas pares → relleno con asteriscos
                fila = "*" + "*" * (ancho - 2) + "*"
            else:
                # filas impares → relleno con espacios
                fila = "*" + " " * (ancho - 2) + "*"
        print(espacios + fila)
