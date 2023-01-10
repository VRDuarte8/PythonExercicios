lista = list()
while True:
    while True:
        n = int(input("Digite um número: "))
        if n in lista:
            print("O número ja existe, digite outro. ")
        else:
            lista.append(n)
            break
    while True:
        continuar = input("Adicionar outro? [S/N] ").strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print(f"Numeros digitados: {sorted(lista)}")
