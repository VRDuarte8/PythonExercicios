print("\033[7m{}SOMA{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)

n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input("Digite um número (999 para parar): "))
    if n != 999:
        soma += n
        cont += 1
print("A soma dos {} números digitados é {}".format(cont, soma))

