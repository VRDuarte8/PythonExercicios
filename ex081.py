lista = list()
cont = 0
cont5 = 0
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    cont += 1
    if n == 5:
        cont5 += 1
    while True:
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
lista.sort(reverse=True)
print("---" * 20)
print(f"""Quantidade de números digitados: {cont}
Números digitados (em ordem decrescente): {lista}""")
if 5 in lista:
    print(f"O número 5 foi digitado {cont5} vezes.")
else:
    print("O número 5 não foi digitado")