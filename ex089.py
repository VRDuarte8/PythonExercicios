print(f"\033[7m{' ' * 20}BOLETIM{' ' * 20}\033[m")
print("---" * 20)

cont = 1
boletim = list()

while True:
    print(f"{' ' * 20}Aluno {cont}")
    nome = (input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    cont += 1
    while True:
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print("-=-"*20)
print(f"No. {'NOME': <10} {'MÉDIA': >10}")
print("---"*10)
for i, a in enumerate(boletim):
    print(i+1,end='   ')
    print(f"{a[0]: <10}", end='')
    print(f" {a[2]: >10.2f}")

while True:
    print("---" * 10)
    n = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if n == 999:
        print("Finalizando...")
        break
    if 0 < n <= len(boletim):
        print(f"As notas de {boletim[n-1][0]} são {boletim[n-1][1]}")