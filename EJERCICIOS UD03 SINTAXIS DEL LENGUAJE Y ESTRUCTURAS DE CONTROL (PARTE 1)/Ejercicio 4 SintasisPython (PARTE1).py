# * 4. Ejercicio - Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta, producto y división.

# * Solicita los dos números al usuario.
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número "))

# * Calculo de todas las variaciones.
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

# * Verificación de que el segundo número no sea cero antes de dividir.
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# * Mostrar los resultados.
print("Suma:", suma)
print("Resta:", resta)
print("Producto", producto)
print("División", division)
