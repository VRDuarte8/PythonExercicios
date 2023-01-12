from random import randint
from time import sleep

print(f"\033[7m{' ' * 20}JOGUE NA MEGA SENA{' ' * 20}\033[m")
print("---" * 20)

jogo = list()
megatotal = list()
num = 0
j = int(input("Número de jogos: "))
for m in range(0, j):
    for v in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break
    megatotal.append(jogo[:])
    jogo.clear()
print(f"Gerando dicas de palpites para {j} jogos: ")
for m in range(0, j):
    sleep(1)
    print(f"Jogo {m+1}: {megatotal[m]}")
