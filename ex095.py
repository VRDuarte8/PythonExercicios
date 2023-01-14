jogadores = []

while True:
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
    jogadores.append(jogador.copy())

    while True:
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print("-="*30)
print('cod ', end='')
for j in jogador.keys():
    print(f'{j:<15}',end='')
print()
print("---"*20)
for k, v in enumerate(jogadores):
    print(f'{k+1:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print("---"*20)
while True:
    while True:
        jog = int(input("Mostrar dados de qual jogador? (999 para sair): "))
        if 0 < jog <= len(jogadores) or jog == 999:
            break
        else:
            print(f"ERRO! Não existe jogador com código {jog}! Tente novamente.")
    if jog == 999:
        break
    print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[jog-1]['nome']}:")
    for i, g in enumerate(jogadores[jog-1]['gols']):
            print(f"   No jogo {i+1} fez {g} gols.")
    print("---"*20)
print("Finalizando...")