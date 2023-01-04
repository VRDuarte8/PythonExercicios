from random import randint
from time import sleep

escolhido = randint(0, 5)
print('---' * 20)
palpite = int(input("Um número entre 0 e 5 foi escolhido, qual o seu palpite? "))
if palpite < 0 or palpite > 5:
    print("\033[1;31mEscolha um número entre 0 e 5")
else:
    print("E o resultado foi.....")
    sleep(3)
    if escolhido == palpite:
        print("\033[1;36mVocê acertou, Parabéns!")
    else:
        print("\033[1;31mVocê errou, o número correto é {}. Tente novamente!".format(escolhido))
