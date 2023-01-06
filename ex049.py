print("\033[7m{}TABUADA{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
n = int(input("Escolha um número: "))
print("\n{}TABUADA DO {}{}".format(" " * 20, n, " " * 20))
for c in range(1, 11):
    print("\033[m{} X {} = \033[1m{}".format(n, c, n * c))
