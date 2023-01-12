numeros = [[], []]

for c in range(0, 7):
    num = int(input(f"Digite o {c + 1}º número: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f"Números: {numeros}")
print(f"Pares: {sorted(numeros[0])}")
print(f"Ímpares: {sorted(numeros[1])}")

