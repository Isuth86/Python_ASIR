# Ejercicio 5 * Escriba un programa que toma como dato de entrada un número que corresponde a la
# longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
# de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
# círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera
# que corresponde con dicho radio.

pi = 3.141592653589793

radio = float(input("Ingrese la longitud del radio: "))

diametro = 2 * radio
circunferencia = pi * diametro
area = pi * (radio ** 2)
volumen = (4/3) * pi * (radio ** 3)

print(f"Longitud de la circunferencia: {circunferencia:.2f}")
print(f"Área del círculo: {area:.2f}")
print(f"Volumen de la esfera: {volumen:.2f}")
