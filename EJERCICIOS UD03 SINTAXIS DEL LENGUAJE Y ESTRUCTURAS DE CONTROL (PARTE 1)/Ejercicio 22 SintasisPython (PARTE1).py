# Ejercicio 22: Escriba un programa que recibe como datos de entrada una hora expresada en horas, minutos y segundos que nos cálcula y escribe la hora, minutos y segundos que serán, transcurrido un segundo.

# Entrada de datos
hora = int(input("Introduce las horas (0-23): "))
minutos = int(input("Introduce los minutos (0-59): "))
segundos = int(input("Introduce los segundos (0-59): "))

# Sumar un segundo
segundos += 1

if segundos == 60:
    segundo = 0
    minutos += 1

if minutos == 60:
    minuto = 0
    hora += 1

    if hora == 24:
        hora = 0

# Resultado
print(
    f"La hora dentro de un segundo será: {hora:2d}:{minutos:02d}:{segundos:02d}")
