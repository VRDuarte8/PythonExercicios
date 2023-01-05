from datetime import date

print("\033[7m{}ALISTAMENTO MILITAR{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
anonasc = int(input("Digite o ano de nascimento: "))
idade = date.today().year - anonasc

if idade < 18:
    print("Você deverá se alistar em {} anos.".format(18 - idade))
elif idade == 18:
    print("Você deve se alistar!")
elif idade > 18:
    print("Seu alistamento foi ou deveria ter sido realizado há {} anos.".format(idade - 18))
