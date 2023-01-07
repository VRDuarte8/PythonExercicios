print("\033[7m{}MÉDIA{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)

maior = 0
menor = 0
soma = 0
cont = 0
continuar = ''
while continuar != 'N':
    n = int(input("Digite um número: "))
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    cont += 1
    continuar = ''
    while continuar != 'N' and continuar != 'S':
        continuar = input("Digitar outro [N/S]? ").upper()
print("Média dos {} valores digitados: {}".format(cont, soma/cont))
print("Menor número digitado: {}".format(menor))
print("Maior número digitado: {}".format(maior))
