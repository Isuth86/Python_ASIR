# Ejercicio 25: La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
# postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre el importe,
# la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el control switch)


# Entrada de datos
nombre = input("Ingrese el nombre del postulante: ")
facultad = input(
    "Ingrese la facultad (ingenieria / derecho / medicina): ").lower()

# Valores por facultad (puedes ajustarlos)
# importe = matrícula
# mensualidad = pago mensual
match facultad:
    case "ingenieria":
        importe = 1500
        mensualidad = 850
    case "derecho":
        importe = 1300
        mensualidad = 900
    case "medicina":
        importe = 2000
        mensualidad = 1200
    case _:
        print("Facultad no válida.")
        exit()

# Cálculo del IGV y monto final
subtotal = importe + mensualidad
igv = subtotal * 0.18
total = subtotal + igv

# Salida de datos
print("\n--- Detalle de matrícula ---")
print("Postulante:", nombre)
print("Facultad:", facultad.capitalize())
print(f"Importe de matrícula: {importe:.2f} €")
print(f"Mensualidad: {mensualidad:.2f} €")
print(f"IGV (18%): {igv:.2f} €")
print(f"Monto final a pagar: {total:.2f} €")
