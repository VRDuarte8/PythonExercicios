salario = float(input("Digite o seu salário atual: "))
if salario > 1250:
    aumento = salario * 0.1
    novosalario = salario + aumento
else:
    aumento = salario * 0.15
    novosalario = salario + aumento
print("Você receberá um aumento de R${:.2f}, novo salário: {}".format(aumento, novosalario))
