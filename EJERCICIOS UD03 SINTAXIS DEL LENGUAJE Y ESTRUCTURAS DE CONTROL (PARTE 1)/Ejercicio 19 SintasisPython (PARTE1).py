# Ejercicio 19: Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares, con el siguiente menú de opciones:
# Bienvenido a su Cajero Virtual
# 1. Ingresar dinero en cuenta
# 2. Retirar dinero de la cuenta
# 3. Salir.

saldo = 1000  # Saldo inicial

while True:
    print("\n--- Bienvenido a su Cajero Virtual ---")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = float(input("¿Cuánto dinero desea ingresar?: "))
        saldo += cantidad
        print(f"Has ingresado ${cantidad}. Saldo actual: ${saldo}")

    elif opcion == "2":
        cantidad = float(input("¿Cuánto dinero desea retirar?: "))
        if cantidad > saldo:
            print("Fondos insuficientes. No se puede realizar el retiro.")
        else:
            saldo -= cantidad
            print(f"Has retirado ${cantidad}. Saldo actual: ${saldo}")

    elif opcion == "3":
        print("Gracias por utilizar el cajero. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
