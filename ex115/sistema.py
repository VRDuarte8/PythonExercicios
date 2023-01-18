from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        titulo("PESSOAS CADASTRADAS")
        lerArquivo(arq)
        sleep(2)
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        titulo("Saindo do sistema... Até logo!")
        break
    else:
        print(f"{cores('ERRO! Digite uma opção válida!', 1, True)}")
