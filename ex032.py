from datetime import date

ano = int(input("Digite um ano (\033[4;35m0 para verificar o ano atual\033[m): "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\033[1;34m{} é um ano bissexto!".format(ano))
else:
    print("\033[1;31m{} não é um ano bissexto!".format(ano))
