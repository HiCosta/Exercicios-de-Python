lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input('Digite um valor para adicioná-lo à lista: ')))
    mais = input('Quer continuar? [S/N]: ')
    while mais in 'Ss':
        lista.append(int(input('Digite um valor para adicioná-lo à lista: ')))
        mais = input('Quer continuar? [S/N]: ')
    while mais not in 'SsNn':
        print('Opção inválida.', end='')
        mais = input('Quer continuar? [S/N]: ')
    if mais in 'Nn':
        print('Encerrando lista...')
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    else:
        listaImpar.append(v)
print(f'{lista}\n{listaPar}\n{listaImpar}')
