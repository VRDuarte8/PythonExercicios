print(f"\033[7m{' ' * 20}CAIXA ELETRÔNICO{' ' * 20}\033[m")
print("---" * 20)

valor = int(input("Valor a ser retirado: R$"))
ced = 50
totced = 0

print("Serão entregues:")
while True:
    if valor >= ced:
        valor -= ced
        totced +=1
    else:
        print(f"{totced} cédulas de R${ced:.2f}")
        totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        else:
            break
