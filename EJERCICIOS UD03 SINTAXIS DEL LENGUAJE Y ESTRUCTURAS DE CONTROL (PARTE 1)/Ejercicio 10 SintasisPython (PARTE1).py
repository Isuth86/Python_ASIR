# Ejercicio 10 * Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta, producto y división (Ten en cuenta la división por cero).

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

if num2 != 0:
    division = num1 / num2
    print(f"División: {division:.2f}")
else:
    print("División: No se puede dividir entre cero")

# Salida de resultados
print(f"Suma: {suma:.2f}")
print(f"Resta: {resta:.2f}")
print(f"Producto: {producto:.2f}")
