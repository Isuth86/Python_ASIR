# Ejercicio 4 Un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
# producto y división.
# Programa que lee dos números y muestra sus operaciones básicas

# Pedimos los números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Calculamos las operaciones
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

# Para la división, controlamos el caso de división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# Mostramos los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("División:", division)
