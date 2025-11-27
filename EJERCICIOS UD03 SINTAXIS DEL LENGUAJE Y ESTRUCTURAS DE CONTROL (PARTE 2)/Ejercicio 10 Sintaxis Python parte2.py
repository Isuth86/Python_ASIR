# Ejercicio 10: Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales.
# Suma y producto de los 10 primeros números naturales

suma = 0
producto = 1

for i in range(1, 11):  # del 1 al 10 inclusive
    suma += i
    producto *= i

print("La suma de los 10 primeros números naturales es:", suma)
print("El producto de los 10 primeros números naturales es:", producto)
