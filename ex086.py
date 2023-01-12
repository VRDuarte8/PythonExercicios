matriz = list()
linha = list()
for c in range(0, 3):
    for l in range(0, 3):
        linha.append(int(input(f"Digite o valor para [{c}, {l}]: ")))
    matriz.append(linha[:])
    linha.clear()

print("---"*20)
print(f"{'MATRIZ':^10}")
for c in range(0, 3):
    for l in range(0, 3):
        print(f"[{matriz[c][l]:^5}]",end=' ')
    print()
