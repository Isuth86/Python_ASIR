# Ejercicio 20: Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la calificación alfabética, escribiendo el siguiente resultado (switch).

# De 0 a <3: Muy Deficiente.
# De 3 a <5: Insuficiente.
# De 5 a <6: Suficiente.
# De 6 a <7: Bien.
# De 7 a <9: Notable.
# De 9 a 10: Sobresaliente.

Nota = float(input("Introduce una calificación entre 0 y 10: "))

if 0 <= Nota < 3:
    print("Muy Deficiente")
elif 3 <= Nota < 5:
    print("Insuficiente")
elif 5 <= Nota < 6:
    print("Suficiente")
elif 6 <= Nota < 7:
    print("Bien")
elif 7 <= Nota < 9:
    print("Notable")
elif 9 <= Nota <= 10:
    print("Sobresaliente")
else:
    print("Nota fuera de rango")
