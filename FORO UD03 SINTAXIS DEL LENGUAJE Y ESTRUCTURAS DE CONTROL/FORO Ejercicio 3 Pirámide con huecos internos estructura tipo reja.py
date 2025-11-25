# *Ejercicio 3: Pirámide con huecos internos (estructura tipo "reja").
# Enunciado: Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.
# Figura para n=6:
try:
    n = int(input("Introduce la altura de la pirámide con huecos internos: "))

    if n <= 0:
        raise ValueError("La altura debe ser un número entero positivo.")
except ValueError as e:
    print(f"Error: {e}")
    print("Debes introducir un número entero positivo.")

else:
