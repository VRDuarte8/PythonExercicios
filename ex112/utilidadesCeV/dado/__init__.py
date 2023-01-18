def leiaDinheiro(f):
    while True:
        num = input(f).strip().replace(',', '.')
        if num.isalpha() or num == '':
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")
        else:
            break
    return float(num)


def leiaInt(f):
    num = input(f)
    while not num.isnumeric():
        print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")
        num = input(f)
    return num

