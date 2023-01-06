print("\033[7m{}MAIOR E MENOR PESO{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)

maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input("Digite o peso da {}º pessoa: ".format(c+1)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print("Maior peso: {}Kg\nMenor peso: {}Kg".format(maior, menor))
