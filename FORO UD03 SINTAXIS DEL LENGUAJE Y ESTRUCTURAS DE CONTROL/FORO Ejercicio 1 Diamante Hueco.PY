# * Ejercicio 1: Diamante Hueco.
# Enunciado: Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.
# Figura para n=5:
def diamante_hueco_corregido(n):
    """
    Imprime un diamante hueco de altura total 2n - 1.
    """
    if n <= 0:
        return

    # La altura total del diamante y el ancho máximo de la línea son 2n - 1
    altura_total = 2 * n - 1
    centro_vertical = n - 1  # El índice de la fila central

    # El bucle principal recorre cada fila del diamante (i de 0 a 2n - 2)
    for i in range(altura_total):

        # 1. Distancia Vertical al Centro (Simetría)
        # Esto determina la 'forma' de la figura (más ancho o más estrecho).
        distancia_al_centro = abs(i - centro_vertical)

        # 2. Número de Espacios Iniciales
        # El número de espacios de indentación es igual a la distancia al centro.
        num_espacios_inicio = distancia_al_centro

        # 3. Ancho de la figura (sin incluir la indentación)
        # El ancho de la figura va de 1 (arriba/abajo) a 2n - 1 (centro).
        # Ancho_figura = 2 * (n - 1 - distancia_al_centro) + 1
        ancho_figura = altura_total - 2 * distancia_al_centro

        # Iniciar la línea con la indentación
        linea = " " * num_espacios_inicio

        # 4. Imprimir la figura
        if ancho_figura == 1:
            # Filas superior, inferior y central (tienen un ancho de 1)
            linea += "*"
        else:
            # Filas intermedias (tienen un ancho > 1)
            # Imprimir el primer '*'
            linea += "*"

            # El número de espacios internos es el ancho total de la figura menos los dos asteriscos.
            num_espacios_internos = ancho_figura - 2

            # Imprimir los espacios internos
            linea += " " * num_espacios_internos

            # Imprimir el segundo '*'
            linea += "*"

        print(linea)


# Ejemplo para n=5
n_ejemplo = 5
print(f"Resultado para n={n_ejemplo}:")
diamante_hueco_corregido(n_ejemplo)
