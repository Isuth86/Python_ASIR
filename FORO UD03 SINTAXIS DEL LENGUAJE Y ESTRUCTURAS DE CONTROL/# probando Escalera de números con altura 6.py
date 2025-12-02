# Escalera de números con altura 6

altura = 11

for i in range(1, altura + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("")
print("Número en orden inverso: ")
print("")

for i in range(altura, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
