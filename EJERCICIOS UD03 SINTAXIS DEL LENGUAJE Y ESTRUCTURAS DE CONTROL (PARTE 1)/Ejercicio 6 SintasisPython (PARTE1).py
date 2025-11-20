# Ejercicio 6 * Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
# el porcentaje de descuento realizado.
precio_original = float(input("Ingrese el precio original del artículo: "))
precio_venta = float(input("Ingrese el precio de venta real: "))

descuento = ((precio_original - precio_venta) / precio_original) * 100

print(f"El porcentaje de descuento realizado es: {descuento:.2f}")
