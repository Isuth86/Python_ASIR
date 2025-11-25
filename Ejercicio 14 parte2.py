# *Ejercicio 14
# Crea una aplicación que dibuje una piramide de asteriscos. Nosotros le pasamos la altura de la pirámide por teclado.
def dibujar_piramide(altura):
    """
    Dibuja una pirámide de asteriscos de la altura especificada.
    """
    print(f"Dibujando una pirámide de altura: {altura}")
    print("-" * 30)

    # El bucle externo recorre cada fila desde 1 hasta la altura
    for i in range(1, altura + 1):
        # 1. Calcular los espacios: (altura - número_de_fila)
        # Esto crea la indentación necesaria para centrar la pirámide
        espacios = " " * (altura - i)

        # 2. Calcular los asteriscos: (2 * número_de_fila - 1)
        # Cada fila impar (1, 3, 5, 7...) garantiza la forma de pirámide
        asteriscos = "*" * (2 * i - 1)

        # 3. Imprimir la fila: espacios + asteriscos
        print(espacios + asteriscos)

# --- Bloque principal del programa ---


while True:
    try:
        # Pedir al usuario la altura de la pirámide
        entrada = input(
            "Introduce la altura de la pirámide (un número entero positivo): ")

        # Intentar convertir la entrada a un entero
        altura_piramide = int(entrada)

        # Validar que la altura sea un número positivo
        if altura_piramide > 0:
            dibujar_piramide(altura_piramide)
            break  # Salir del bucle si la entrada es válida
        else:
            print("❌ La altura debe ser un número entero positivo mayor que cero.")

    except ValueError:
        # Capturar el error si la entrada no es un número entero
        print(f"⚠️ Error: '{entrada}' no es un número entero válido.")

print("\n✨ Programa terminado.")
