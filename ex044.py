from time import sleep

valor = float(input("Valor do produto: "))
condicao = input("Escolha o método de pagamento:\n"
                 "[ 1 ] à vista no dinheiro/cheque (10% de desconto)\n"
                 "[ 2 ] à vista no cartão (5% de desconto)\n"
                 "[ 3 ] Em 2x no cartão (sem juros)\n"
                 "[ 4 ] 3x ou mais no cartão (20% de juros)\n")
sleep(1)
if condicao == '1':
    valor = valor * 0.9
    print("Valor a ser pago: \033[1mR${:.2f}".format(valor))
elif condicao == '2':
    valor = valor * 0.95
    print("Valor a ser pago: \033[1mR${:.2f}".format(valor))
elif condicao == '3':
    parcelado = valor / 2
    print("Valor a ser pago: \033[1mR${:.2f} (2x de R${:.2f})".format(valor, parcelado))
elif condicao == '4':
    parcelamento = int(input("Selecione o parcelamento (3x ou mais): "))
    sleep(1)
    if parcelamento < 3:
        print("Parcelamento inválido")
    else:
        juros = valor * 0.2 * parcelamento
        valor = valor + juros
        parcelado = valor/parcelamento
        print("Valor a ser pago: \033[1mR${:.2f} ({}x de R${:.2f})".format(valor, parcelamento, parcelado))
else:
    print("\033[1;31mCondição de Pagamento Inválida")
