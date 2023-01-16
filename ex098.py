from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if passo == 0:
        passo = 1
    if inicio > fim:
        fim = fim-1
        if passo > 0:
            passo *= -1
    else:
        fim = fim+1
    for n in range(inicio, fim, passo):
        print(n, end=' ')
        sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print("Contagem Personalizada!")
contador(
    int(input("Início: ")),
    int(input("Fim: ")),
    int(input("Passo: ")))
