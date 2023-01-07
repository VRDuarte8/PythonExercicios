from time import sleep

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
menu = 0
while menu != 5:
    print("---" * 20)
    menu = int(input("""O que você deseja fazer com estes números?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] Ver o maior
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa
    """))
    sleep(1)
    if menu == 1:
        print("A soma de \033[1m{}\033[m e \033[1m{}\033[m é igual a \033[1m{}\033[m."
              .format(n1, n2, n1 + n2))
    elif menu == 2:
        print("\033[1m{}\033[m multiplicado por \033[1m{}\033[m é igual a \033[1m{}\033[m."
              .format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print("\033[1m{}\033[m é o maior número.".format(n1))
        elif n1 < n2:
            print("\033[1m{}\033[m é o maior número.".format(n2))
        elif n1 == n2:
            print("Ambos os números são iguais (\033[1m{}\033[m)".format(n1))
    elif menu == 4:
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
    elif menu == 5:
        print("Finalizando...")
    elif menu < -1 or menu > 5:
        print("\033[1;31mOpção inválida!\033[m")
    sleep(2)
