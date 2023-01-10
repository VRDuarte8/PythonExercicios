lista = list()
for v in range(0, 5):
    lista.append(int(input(f"Digite o valor da posição {v}: ")))
maior = max(lista)
menor = min(lista)
print(f"Lista final: {lista}")
print(f"Maior número: {maior} / Posição: ", end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f"{pos}º...", end='')
print(f"\nMenor número: {menor} / Posição: ", end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f"{pos}º...", end='')
