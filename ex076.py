print(f"\033[7m{'LISTA DE PRODUTOS':^40}\033[m")
print("---" * 20)

produtos = ('Processador', 2000,
            'Placa-mãe', 1200,
            'Memória', 400,
            'Placa de vídeo', 3000,
            'Water Cooler', 400,
            'Gabinete', 200,
            'SSD', 200,
            'Fonte', 100,
            'Teclado', 200,
            'Mouse', 200,
            'Monitor', 2000)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}", end='')
    else:
        print(f"R${produtos[pos]:>8.2f}")
print("---" * 20)