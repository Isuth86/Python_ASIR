def ala_delta(n):
    # Triángulo superior
    for i in range(n):
        espacios = " " * (n - i - 1)
        if i == 0:
            print(espacios + "*")
        elif i == 1:
            print(espacios + "**")
        else:
            hueco = " " * (i - 1)
            print(espacios + "*" + hueco + "*")

    # Triángulo inferior (invertido)
    for i in range(n - 2, -1, -1):
        espacios = " " * (n - i - 1)
        if i == 0:
            print(espacios + "*")
        elif i == 1:
            print(espacios + "**")
        else:
            hueco = " " * (i - 1)
            print(espacios + "*" + hueco + "*")


ala_delta(5)
