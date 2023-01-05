valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
prazo = float(input("Em quantos anos será quitado o empréstimo? "))

prestacao = (valor / prazo) / 12
if prestacao > salario * 0.3:
    print("Empréstimo de R${:.2f} \033[1;31mNEGADO\033[m! ".format(valor), end='')
    print("A prestação mensal de R${:.2f} excede 30% do salário.".format(prestacao))
else:
    print("Empréstimo de R${:.2f} \033[1;32mAPROVADO\033[m! "
          "A prestação mensal será de R${:.2f}.".format(valor, prestacao))
