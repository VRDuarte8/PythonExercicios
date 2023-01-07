print("\033[7m{}PROGRESSÃO ARITMÉTICA{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
n = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
cont = 1
print("PA = ", end='')
while cont <= 10:
    print(n, end=' -> ')
    n += r
    cont += 1
print("FIM")
