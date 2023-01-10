lista = list()
listaimpar = list()
listapar = list()

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    while True:
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

for pos, valor in enumerate(lista):
    if valor % 2 == 0:
        listapar.append(lista[pos])
    else:
        listaimpar.append(lista[pos])

print(f"""Lista completa: {lista}
Lista pares: {listapar}
Lista ímpares: {listaimpar}""")
