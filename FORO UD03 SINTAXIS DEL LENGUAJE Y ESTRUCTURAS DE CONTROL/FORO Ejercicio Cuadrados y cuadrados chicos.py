def cuadrado_rejilla_cerrado(n, simbolo="*"):
    for fila in range(n):
        if fila % 2 == 0:
            # Fila de asteriscos seguidos
            print((simbolo + " ") * n + simbolo)
        else:
            # Fila de asteriscos separados
            linea = ""
            for col in range(n+1):
                linea += simbolo + "   "
            print(linea.strip())


# Ejemplo: altura 8
cuadrado_rejilla_cerrado(8)
