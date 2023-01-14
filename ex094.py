pessoa = dict()
cadastros = list()
mulheres = list()
idadeacima = list()
soma = 0
cont = 0

while True:
    print("---" * 20)
    print(f"{'CADASTRO':^40}")
    pessoa['nome'] = input("Nome: ")
    while True:
        pessoa['sexo'] = input("Sexo [M/F]: ").strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    cont += 1
    cadastros.append(pessoa.copy())
    while True:
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

media = soma/cont
for c in cadastros:
    for k, v in c.items():
        if k == 'sexo' and v == 'F':
            mulheres.append(c.copy())
        if k == 'idade' and v > media:
            idadeacima.append(c.copy())

print("---"*20)
print(f"""- Pessoas cadastradas: {cont}
- Média de idade: {media:.2f}
- Mulheres: """, end='')
for m in mulheres:
    for k, n in m.items():
        if k == 'nome':
            print(n, end=' ')
print("\n- Pessoas com idade acima da média: ")
for i in idadeacima:
    print()
    for k, v in i.items():
        print(f"{k} = {v};", end=' ')

print("\n<< ENCERRADO >>")
