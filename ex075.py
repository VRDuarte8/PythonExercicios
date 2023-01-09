tupla = (int(input("1º valor: ")), int(input("2º valor: ")),
         int(input("3º valor: ")), int(input("4º valor: ")))
print(f"Tupla = {tupla}")

if 9 not in tupla:
    print("O número 9 não foi digitado")
else:
    print(f"Aparições do número 9: {tupla.count(9)}")

if 3 not in tupla:
    print("O número 3 não foi digitado")
else:
    print(f"Posição do primeiro número 3: {tupla.index(3) + 1}º")

print(f"Números pares: ", end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
