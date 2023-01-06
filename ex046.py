from time import sleep

print("\033[7m{}CONTAGEM REGRESSIVA{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("\033[1;35m*Fogos*")