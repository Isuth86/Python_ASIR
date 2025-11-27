# Ejercicio 24: Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día de la semana;
# sí el día es martes o jueves, se realizará un descuento del 15% por la compra.
# Visualizar el descuento y el total a pagar por la compra.

# Entrada de datos
monto = float(input("Ingrese el monto de la compra (€): "))
dia = input("Ingrese el día de la semana: ").lower()

# Cálculo del descuento
if dia == "martes" or dia == "jueves":
    descuento = monto * 0.15
else:
    descuento = 0

total = monto - descuento

# Salida
print(f"\nDescuento aplicado: {descuento:.2f} €")
print(f"Total a pagar: {total:.2f} €")
