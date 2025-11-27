# Ejercicio 26: En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
# en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
# Si los tres dados son seis, mostrar el mensaje “Excelente”
# Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
# Si un dado se obtiene seis, mostrar el mensaje “Regular”
# Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
# (Use el control switch).

# Entrada de datos: lanzamiento de tres dados
dado1 = int(input("Lanzamiento dado 1 (1-6): "))
dado2 = int(input("Lanzamiento dado 2 (1-6): "))
dado3 = int(input("Lanzamiento dado 3 (1-6): "))

# Contar cuántos seises
seises = 0
for dado in [dado1, dado2, dado3]:
    if dado == 6:
        seises += 1

# Mostrar mensaje según la cantidad de seises
match seises:
    case 3:
        print("Excelente")
    case 2:
        print("Muy bien")
    case 1:
        print("Regular")
    case 0:
        print("Pésimo")
