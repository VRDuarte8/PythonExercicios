def leiaInt(f):
    num = input(f)
    while not num.isnumeric():
        print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")
        num = input(f)
    return num


n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")