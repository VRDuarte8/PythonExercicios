contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
            'vinte')

while True:
    while True:
        n = int(input("Digite um número entre 0 e 20: "))
        if 0 <= n <= 20:
            break
    while True:
        continuar = input(f'Você digitou {contagem[n]}, continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break


