print(f"\033[7m{' ' * 20}BRASILEIRÃO 2022{' ' * 20}\033[m")
print("---" * 20)
tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR',
          'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
          'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(f"5 primeiros colocados: {tabela[:5]}")
print(f"Rebaixados: {tabela[-4:]}")
print(f"Times em ordem alfabética: {sorted(tabela)}")
print(f"Posição do Corinthains: {tabela.index('Corinthians') + 1}º")
