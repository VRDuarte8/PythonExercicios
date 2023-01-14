from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
rank = list()
print("Valores sorteados: ")
for k, v in jogo.items():
    print(f"O {k} tirou {v}")
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('---'*20)
print(" -- Ranking dos jogadores --")
for i, v in enumerate(rank):
    print(f"   {i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)