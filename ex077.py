print(f"\033[7m{' ' * 20}VOGAIS{' ' * 20}\033[m")
print("---" * 20)

palavras = ('Amor', 'Amizade', 'Raiva', 'Tristeza', 'Ira', 'Paixao')
for p in range(0, len(palavras)):
    cont = 0
    print(palavras[p], end=' = ')
    for l in palavras[p]:
        if l in 'AaEeIiOoUu':
            print(l, end=' ')
    print("")
