# Ejercicio 15 * Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales son iguales.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")

if num1 == num2 == num3:
    print("Los tres números son iguales")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("hay al menos dos números iguales")
else:
    print("Los tres números son diferentes")
