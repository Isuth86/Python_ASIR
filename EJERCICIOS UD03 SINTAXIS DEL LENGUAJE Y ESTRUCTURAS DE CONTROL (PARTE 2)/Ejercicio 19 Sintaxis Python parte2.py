# Ejercicio 19: Programa donde el usuario "piensa" un número del 1 al 100 y el ordenador intenta
# adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el
# usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado).

print("Piensa un número entre 1 y 100 (no lo digas).")
print("Yo intentaré adivinarlo. Responde con:")
print("  'mayor' si tu número es mayor")
print("  'menor' si tu número es menor")
print("  'igual' si lo he adivinado")

inferior = 1
superior = 100
intentos = 0

while True:
    intentos += 1
    propuesta = (inferior + superior) // 2
    print(f"¿Es {propuesta}?")
    respuesta = input("Tu respuesta: ").strip().lower()

    if respuesta == "igual":
        print(f"¡Genial! He adivinado tu número en {intentos} intentos.")
        break
    elif respuesta == "mayor":
        inferior = propuesta + 1
    elif respuesta == "menor":
        superior = propuesta - 1
    else:
        print("Respuesta no válida. Escribe 'mayor', 'menor' o 'igual'.")

    if inferior > superior:
        print("Ups... parece que hubo un error en las respuestas.")
        break
