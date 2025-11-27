# Ejercicio 21: Escriba un programa que calcula el salario neto semanal de un trabajador en función del número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
# Las primeras 35 horas se pagan a tarifa normal.
# Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
# Las tasas de impuesto son:
# Los primeros 500€ son libres de impuestos.
# Los siguientes 400€ tiene un 25% de impuesto.
# Los restantes un 45% de impuesto.

# Escribe el nombre del trabajador,salario bruto, tasas y salario neto:

# Pedir datos al usuario
nombre = input("Introduce el nombre del trabajador: ")
horas = float(input("Horas trabajadas en la semana: "))
tarifa = float(input("Tarifa por hora (€): "))

# Cálculo del salario bruto
if horas <= 35:
    salario_bruto = horas * tarifa
else:
    horas_extra = horas - 35
    salario_bruto = (35 * tarifa) + (horas_extra * tarifa * 1.5)

# Cálculo de impuestos
if salario_bruto <= 500:
    impuestos = 0
elif salario_bruto <= 900:
    impuestos = (salario_bruto - 500) * 0.25
else:
    impuestos = (400 * 0.25) + ((salario_bruto - 900) * 0.45)

# Salario neto
salario_neto = salario_bruto - impuestos

# Mostrar resultados
print("n--- Nómina semanal ---")
print(f"Trabajador:", nombre)
print(f"Salario bruto: {salario_bruto:.2f} €")
print(f"Tasas (impuestos): {impuestos:.2f} €")
print(f"Salario neto: {salario_neto:.2f} €")
