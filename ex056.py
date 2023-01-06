maioridade = 0
media = 0
menorvinte = 0
maisvelho = ' '
for c in range(0, 4):
    print("---" * 20 + "{}º pessoa".format(c+1) + "---" * 20)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = int(input("Sexo ([ 1 ] Masculino / [ 2 ] Feminino): "))
    media = media + idade
    if idade > maioridade and sexo == 1:
        maioridade = idade
        maisvelho = nome
    if idade < 20 and sexo == 2:
        menorvinte += 1

if maioridade == 0:
    maisvelho = "Sem homens"

print("---" * 44)
print("""Média de idade: {:.2f}
Homem mais velho: {} ({} anos)
Quantidade de mulheres com menos de 20 anos: {}""".format(media/4, maisvelho, maioridade, menorvinte))
