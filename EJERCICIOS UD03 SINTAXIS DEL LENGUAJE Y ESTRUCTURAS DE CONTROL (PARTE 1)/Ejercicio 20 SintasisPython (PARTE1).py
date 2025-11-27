# Ejercicio 20: Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la calificación alfabética, escribiendo el siguiente resultado (switch).

# De 0 a <3: Muy Deficiente.
# De 3 a <5: Insuficiente.
# De 5 a <6: Suficiente.
# De 6 a <7: Bien.
# De 7 a <9: Notable.
# De 9 a 10: Sobresaliente.

calificacion = float(input("Introduce una calificación entre 0 y 10: "))

match calificacion:
    case x if 0 <= x < 3:
        print("Muy Deficiente")
    case x if 3 <= x < 5:
        print("Insuficiente")
    case x if 5 <= x < 6:
        print("Suficiente")
    case x if 6 <= x < 7:
        print("Bien")
    case x if 7 <= x < 9:
        print("Notable")
    case x if 9 <= x <= 10:
        print("Sobresaliente")
    case _:
        print("Calificación fuera de rango")
