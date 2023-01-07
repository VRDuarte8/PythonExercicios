print(f"\033[7m{' ' * 20}TABUADA{' ' * 20}\033[m")
print("---" * 20)

while True:
    n = int(input("Digite o número da tabuada desejado (negativo para parar): "))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
        c += 1
    print("---" * 20)