from random import randint
from time import sleep

print(f"\033[7m{' ' * 20}PAR OU ÍMPAR{' ' * 20}\033[m")
print("---" * 20)

cont = 0
while True:
    escolha = ' '
    n = -1
    computador = randint(0, 10)
    while escolha not in 'PpIi':
        escolha = input("Você escolhe [p] par ou [i] ímpar? ").upper().strip()
    while n < 0 or n > 10:
        n = int(input("Digite seu número (entre 0 e 10): "))
    print("O computador escolhe...", end=' ')
    sleep(3)
    print(computador)
    soma = n + computador
    print(f"{n} + {computador} = {soma}", end=' ')
    if soma % 2 == 0:
        print("(\033[1mPAR\033[m)")
        if escolha == 'P':
            print("\033[1;34mVITÓRIA\033[m")
        else:
            print("\033[1;31mDERROTA\033[m")
            break
    else:
        print("(\033[1mÍMPAR\033[m)")
        if escolha == 'I':
            print("\033[1;34mVITÓRIA\033[m")
        else:
            print("\033[1;31mDERROTA\033[m")
            break
    cont += 1
    print("---" * 20)
print(f"""Fim de jogo!
Vitórias seguidas: {cont}.""")
