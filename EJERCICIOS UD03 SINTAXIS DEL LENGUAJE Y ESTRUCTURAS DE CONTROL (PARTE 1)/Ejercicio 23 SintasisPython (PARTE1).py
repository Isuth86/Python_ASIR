# Ejercicio 23: Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente; si el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta” se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
# según sea el caso y el total a pagar de la compra.

# Entrada de datos
valor_compra = float(input("Ingrese el valor de la compra (€): "))
metodo_pago = input("Método de pago (contado/tarjeta): ").lower()

# Cálculo según el método de pago
if metodo_pago == "contado":
    descuento = valor_compra * 0.05
    total = valor_compra - descuento
    print(f"\nDescuento aplicado: {descuento:.2f} €")
    print(f"Total a pagar: {total:.2f} €")

elif metodo_pago == "tarjeta":
    recargo = valor_compra * 0.03
    total = valor_compra + recargo
    print(f"\nRecargo aplicado: {recargo:.2f} €")
    print(f"Total a pagar: {total:.2f} €")

else:
    print("Método de pago no válido. Use 'contado' o 'tarjeta'.")
