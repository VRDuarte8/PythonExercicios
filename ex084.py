cadastros = list()
maisleves = list()
maispesadas = list()
cont = 0
maior = menor = 0
while True:
    print("---"*20)
    print(f"{'CADASTRO':^40}")
    cadastros.append(input("Nome: "))
    peso = float(input("Peso: "))
    cadastros.append(peso)
    if cont == 0:
        maior = peso
        menor = peso
    if peso >= maior:
        if peso > maior:
            maior = peso
            maispesadas.clear()
        maispesadas.append(cadastros[:])
    if peso <= menor:
        if peso < menor:
            menor = peso
            maisleves.clear()
        maisleves.append((cadastros[:]))
    cadastros.clear()
    cont += 1
    while True:
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print("---"*20)
print(f"Quantidade de cadastros: {cont}")
print(f"O menor peso foi de {menor:.2f}Kg, de ", end='')
for pos, n in enumerate(maisleves):
    print(maisleves[pos][0], end=' ')
print(f"\nO maior peso foi de {maior:.2f}Kg, de ", end='')
for pos, n in enumerate(maispesadas):
    print(maispesadas[pos][0], end=' ')