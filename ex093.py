jogador = {'nome': input("Nome: ")}
partidas = list()
npartidas = int(input("Número de partidas jogadas: "))
tot = 0

for p in range(0, npartidas):
    ngol = int(input(f"Gols na {p+1}º partida: "))
    partidas.append(ngol)
    tot += ngol
jogador['gols'] = partidas.copy()
jogador['total'] = tot

print("---"*20)
print(jogador)
print("---"*20)
for c, v in jogador.items():
    print(f"O campo {c} tem o valor {v}")
print("---"*20)

print(f"O jogador {jogador['nome']} jogou {npartidas}.")
for p in range(0, npartidas):
    print(f"{'=>':>7} Na partida {p+1}, fez {jogador['gols'][p]} gols.")
print(f"Fez um total de {tot} gols.")
