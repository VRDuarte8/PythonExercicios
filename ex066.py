print(f"\033[7m{' ' * 20}SOMA{' ' * 20}\033[m")
print("---" * 20)

n = 0
soma = 0
cont = 0
while True:
    n = int(input("Digite um número (999 para parar): "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"A soma dos {cont} números digitados é {soma}")
