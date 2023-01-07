print("\033[7m{}PROGRESSÃO ARITMÉTICA{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
valor = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
n = 10
aumento = 1
cont = 1
print("PA = ", end='')
while aumento != 0:
    print(valor, end=' -> ')
    valor += r
    cont += 1
    if cont > n:
        cont = 1
        aumento = int(input("Deseja ver mais quantos? (Digite 0 para encerrar) "))
        if aumento < 0:
            aumento = 0
        n = aumento
print("FIM")
