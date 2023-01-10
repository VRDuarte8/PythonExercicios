lista = list()
for c in range(0, 5):
    n = int(input("Digite um número: "))
    pos = -1
    for p, v in enumerate(lista):
        if v >= n:
            pos = p
            break
    if pos == -1:
        print("Adicionado no final da lista...")
        lista.append(n)
    else:
        print(f"Adicionado na posição {pos}")
        lista.insert(pos, n)
print("---" * 20)
print(f"Lista final: {lista}")


