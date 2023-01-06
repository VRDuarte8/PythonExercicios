print("\033[7m{}NÚMERO PRIMO{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
n = int(input("Digite um número: "))
primo = 0
for c in range(1, n):
    if n % c == 0 and c != 1:
        primo = 1
if primo == 1 or n == 1:
    print("Não é um número primo")
else:
    print("É um número primo")
