from random import randint
from time import sleep

escolhido = randint(0, 5)
print('---' * 20)
palpite = int(input("Um número entre 0 e 5 foi escolhido, qual o seu palpite? "))
print("E o resultado foi.....")
sleep(3)
if escolhido == palpite:
    print("Você acertou, Parabéns!")
else:
    print("Você errou, o número correto é {}. Tente novamente!".format(escolhido))
