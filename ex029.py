velocidade = float(input("Qual a velocidade do carro? "))
if velocidade > 80:
    velacima = (velocidade - 80)
    multa = velacima * 7
    print("\033[1;31mO carro foi multado em R${:.2f} por estar {:.2f} Km/h acima da velocidade permitida!"
          .format(multa, velacima))
print("\033[34mLiberado.")
