print("\033[7m{}SEQUÊNCIA DE FIBONACCI{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
n = int(input("Digite o número de elementos da sequência de fibonacci desejado: "))
valor = 0
valorant = 1
cont = 1
aux = 1
while cont != n + 1 and n > 0:
    print(valor, end=' -> ')
    aux = valor
    valor += valorant
    valorant = aux
    cont += 1
print("FIM")