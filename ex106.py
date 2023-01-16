from time import sleep


c = ('\033[m',      #Padrão
     '\033[41m',    #Vermelho
     '\033[42m',    #Verde
     '\033[43m',    #Amarelo
     '\033[44m',    #Azul
     '\033[45m',    #Roxo
     '\033[7m'   #branco
     )


def ajuda(func, cor=6):
    titulo(f"Acessando o manual do comando '{func}'", 4)
    print(c[cor], end='')
    help(func)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam )
    print(f"  {msg}")
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    f = input("\033[mFunção ou Biblioteca > ")
    if f.upper() == 'FIM':
        titulo('ATÉ LOGO', 1)
        break
    ajuda(f)
