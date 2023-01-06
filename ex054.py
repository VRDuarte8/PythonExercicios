from datetime import date

print("\033[7m{}MAIORIDADE{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input("Digite o ano de nascimento da {}º pessoa: ".format(c+1)))
    if date.today().year - ano >= 21:
        maior += 1
    elif date.today().year - ano < 21:
        menor += 1
print("{} pessoas são menores de idade, enquanto {} já atingiram a maioridade".format(menor, maior))
