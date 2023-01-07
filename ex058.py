from random import randint

print("O computador escolheu um número entre 0 e 10, qual ele escolheu? ")
alvo = randint(0, 10)
palpite = -1
cont = 0
while alvo != palpite:
    palpite = int(input(""))
    if alvo != palpite:
        print("\033[1;31mERROU!\033[m Tente outro.")
    cont += 1
print("\033[1;34mACERTOU!\033[m Você precisou de {} palpites para acertar.".format(cont))
