def titulo(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cores(c, 3)} - {cores(item, 4)}')
        c += 1
    print('-' * 40)
    opc = leiaInt(f"{cores('Sua Opção:', 3)} ")
    return opc



def cores(t, c, n=False):
    neg = ''
    if n == True:
        neg = '1;'
    cor = (f'\033[{neg}m',  # Padrão
           f'\033[{neg}31m',  # Vermelho
           f'\033[{neg}32m',  # Verde
           f'\033[{neg}33m',  # Amarelo
           f'\033[{neg}34m',  # Azul
           f'\033[{neg}35m',  # Roxo
           f'\033[{neg}7m'  # Preto
           )
    return f"{cor[c]}{t}{cor[0]}"


def leiaInt(f):
    while True:
        try:
            num = int(input(f))
        except ValueError:
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print("\033[1;31mERRO! O número não foi digitado.\033[m")
            return 0
        except:
            print("\033[1;31mERRO!\033[m")
        else:
            break
    return num
