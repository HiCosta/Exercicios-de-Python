from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resp = menu(['Ver pessoas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('Saindo do sistema...')
        break
    else:
        print('ERRO. Digite uma opção válida.')
    sleep(2)
