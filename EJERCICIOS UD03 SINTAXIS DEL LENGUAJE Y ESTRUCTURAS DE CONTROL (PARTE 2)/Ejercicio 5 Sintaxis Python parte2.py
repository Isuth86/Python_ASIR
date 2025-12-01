# Ejercicio 5: Programa que muestre en líneas separadas lo siguiente:
# ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
# WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A.
import string

# ABECEDARIO INVERSO
cadena = string.ascii_uppercase[::-1]  # "ZYXWVUTSRQPONMLKJIHGFEDCBA"

for i in range(len(cadena)):
    print(cadena[i:])
