# * Ejercicio 1: Diamante Hueco.
# Enunciado: Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.
# Figura para n=5:
n = int(input("Introduce un número: "))

for i in range(1, n+1):
    espacios = " " * (n - i)
    if i == 1:
        print(espacios + "*")
    else:
        vacío = " " * (2*i - 3)
        print(espacios + "*" + vacío + "*")

for i in range(n-1, 0, -1):
    espacios = " " * (n - i)
    if i == 1:
        print(espacios + "*")
    else:
        vacío = " " * (2*i - 3)
        print(espacios + "*" + vacío + "*")
