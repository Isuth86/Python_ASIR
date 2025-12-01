# Ejercicio 20: Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de
# 5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad
# (utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible.
# Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100
# €, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque
# sume 145 € no es el mínimo número de billetes posible).

cantidad = int(input("Introduce la cantidad en euros (múltiplo de 5): "))

if cantidad <= 0 or cantidad % 5 != 0:
    print("Error: Debes introducir un número positivo múltiplo de 5.")
else:
    billetes = [500, 200, 100, 50, 20, 10, 5]
    resultado = {}

    restante = cantidad
    for b in billetes:
        num = restante // b
        if num > 0:
            resultado[b] = num
            restante -= num * b

    print(f"Para {cantidad} € se necesitan:")
    for b in billetes:
        if b in resultado:
            print(f"  {resultado[b]} billete(s) de {b} €")
