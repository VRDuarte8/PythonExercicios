total = 0
cont = 1
maismil = 0
maisbarato = 0
nomebarato = ' '
while True:
    continuar = ' '
    print(f"{' '*20}Produto")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    if cont == 1:
        maisbarato = preco
        nomebarato = nome
    else:
        if preco < maisbarato:
            maisbarato = preco
            nomebarato = nome
    if preco > 1000:
        maismil += 1
    total += preco
    while continuar not in 'SN':
        continuar = input("Cadastrar outro? [S/N} ").strip().upper()[0]
    if continuar == 'N':
        print("---" * 20)
        break
    cont += 1
    print("---" * 20)
print(f"""{cont} produtos cadastrados.
Total: R${total:.2f}
Mais de R$1000.00: {maismil}
Mais barato: {nomebarato} (R${maisbarato:.2f})""")
