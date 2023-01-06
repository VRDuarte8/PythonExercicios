print("\033[7m{}PROGRESSÃO ARITMÉTICA{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
print("PA = ", end='')
for c in range(1, 11):
    an = a1 + (c - 1) * r
    print(an, end=' -> ')
print("FIM")