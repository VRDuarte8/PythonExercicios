n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
maior = n1
menor = n2
if n1 < n2:
    menor = maior
    maior = n2
if maior < n3:
    maior = n3
if menor > n3:
    menor = n3
print("O maior número é o \033[1;36m{}\033[m, enquanto o menor é o \033[1;31m{}\033[m".format(maior, menor))
