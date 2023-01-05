from random import choice
from time import sleep

print("\033[7m{}PEDRA, PAPEL OU TESOURA{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
usuario = input("Você escolhe pedra, papel ou tesoura? ").upper()
escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
if usuario not in escolhas:
    print("\033[1;31mERRO! Escolha Inválida")
else:
    computador = choice(escolhas)
    print("O computador escolhe.... ", end='')
    sleep(3)
    print("\033[1m{}".format(computador))
    print("---" * 20)
    if usuario == 'PEDRA':
        if computador == 'PEDRA':
            print('                         \033[1;33mEMPATE')
        elif computador == 'PAPEL':
            print('                         \033[1;31mDERROTA')
        elif computador == 'TESOURA':
            print('                         \033[1;34mVITÓRIA')
        else:
            print("                         \033[1;31mERRO!")
    elif usuario == 'PAPEL':
        if computador == 'PAPEL':
            print('                         \033[1;33mEMPATE')
        elif computador == 'TESOURA':
            print('                         \033[1;31mDERROTA')
        elif computador == 'PEDRA':
            print('                         \033[1;34mVITÓRIA')
        else:
            print("                         \033[1;31mERRO!")
    else:
        if computador == 'TESOURA':
            print('                         \033[1;33mEMPATE')
        elif computador == 'PEDRA':
            print('                         \033[1;31mDERROTA')
        elif computador == 'PAPEL':
            print('                         \033[1;34mVITÓRIA')
        else:
            print("                         \033[1;31mERRO!")
print("\033[m---" * 20)
