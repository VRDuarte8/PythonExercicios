from time import sleep

print("\033[7m{}FATORIAL{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
n = int(input("Digite um número: "))
resultado = 1
sleep(1)
print("Fatorial de {}:\n{}! = ".format(n, n), end='')
'''while n > 0:
    print(n, end=' ')
    resultado *= n
    n -= 1
    if n == 0:
        print("= {}".format(resultado))
    else:
        print("X", end=' ')'''

for n in range(n, 0, -1):
    print(n, end=' ')
    resultado *= n
    n -= 1
    if n == 0:
        print("= {}".format(resultado))
    else:
        print("X", end=' ')