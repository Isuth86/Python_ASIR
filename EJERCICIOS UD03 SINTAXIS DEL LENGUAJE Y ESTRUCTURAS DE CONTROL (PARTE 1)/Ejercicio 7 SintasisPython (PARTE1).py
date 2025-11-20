# Ejercicio 7 * Escriba un programa que lea un valor correspondiente a una distancia en millas marinas y
# escriba la distancia en metros. Sabiendo que una milla marina equivale a 1.852 metros.


millas_marinas = float(input("Ingrese la distancia en millas marinas: "))


metros = millas_marinas * 1852


print(f"La distancia en metros es: {metros:.2f}")
