matriz = list()
linha = list()
somapar = soma3c = maior2l = 0

for l in range(0, 3):
    for c in range(0, 3):
        linha.append(int(input(f"Digite o valor para [{c}, {l}]: ")))
    matriz.append(linha[:])
    linha.clear()

print("---"*20)
print(f"{'MATRIZ':^10}")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[c][l]:^5}]",end=' ')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
        if c == 0:
            maior2l = matriz[1][c]
        elif matriz[1][c] > maior2l:
            maior2l = matriz[1][c]
    print()
print(f"""Soma dos pares: {somapar}
Soma terceira coluna: {soma3c}
Maior valor da segunda linha: {maior2l}""")