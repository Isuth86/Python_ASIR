# Ejercicio 13 * Escriba un programa que lea dos números y lo visualiza en orden ascendente.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrse el segundo número: "))

if num1 < num2:
    print(f"Orden ascendente: {num1}, {num2}")
elif num2 < num1:
    print(f"Orden ascendente: {num2}, {num1}")
else:
    print("Ambos números son iguales")
