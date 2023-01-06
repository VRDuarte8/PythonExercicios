soma = 0
n = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma += c
        n += 1
print("O resultado da soma dos {} números foi \033[1m{}".format(n, soma))
