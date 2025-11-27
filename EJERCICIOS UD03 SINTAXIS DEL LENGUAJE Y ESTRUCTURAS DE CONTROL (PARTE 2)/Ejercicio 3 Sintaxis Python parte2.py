# Ejercicio 3: Programa que muestre los números pares comprendidos entre el 1 y el 200. Esta vez utiliza
# un contador sumando de 1 en 1.

# Mostrar los números pares entre 1 y 200 usando contador +1

contador = 1

while contador <= 200:
    if contador % 2 == 0:   # condición de par
        print(contador)
    contador += 1
