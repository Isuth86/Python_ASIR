# * Ejercicio 13
# Crea una aplicación que dibuje una escalera de números, siendo cada línea números empezando
# Escalera de números sin control de errores

altura = int(input("Introduce la altura: "))

for i in range(1, altura + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
