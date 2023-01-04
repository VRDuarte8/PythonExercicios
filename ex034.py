salario = float(input("Digite o seu salário atual: "))
if salario > 1250:
    aumento = salario * 0.1
    novosalario = salario + aumento
else:
    aumento = salario * 0.15
    novosalario = salario + aumento
print("Você receberá um aumento de \033[4;32mR${:.2f}\033[m, "
      "novo salário: \033[4;34mR${:.2f}".format(aumento, novosalario))
