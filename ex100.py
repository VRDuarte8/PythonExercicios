from random import randint
from time import sleep


def sorteia(lista):
    print("Números sorteados: ", end='')
    for i in range(0, 5):
        n = randint(1, 100)
        lista.append(n)
        print(n, end=' ')
        sleep(0.3)
    print()


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f"A soma dos pares entre {lista} é igual a {soma}")


numeros = list()
sorteia(numeros)
somaPar(numeros)
