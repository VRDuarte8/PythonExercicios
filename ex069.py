cont = 1
maior = 0
hom = 0
mulmenvinte = 0
while True:
    sexo = ' '
    continuar = ' '
    print(f"{' '* 20}{cont}º Pessoa")
    idade = int(input("Idade: "))
    if idade > 18:
        maior += 1
    while sexo not in 'MF':
        sexo = input("Sexo [M/F]: ").strip().upper()[0]
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mulmenvinte += 1
    while continuar not in 'SN':
        continuar = input("Cadastrar outra pessoa? [S/N] ").strip().upper()[0]
    if continuar == 'N':
        print("---" * 20)
        break
    cont += 1
    print("---" * 20)
print(f"""Mais de 18 anos: {maior}
Homens: {hom}
Mulheres com menos de 20 anos: {mulmenvinte}""")

