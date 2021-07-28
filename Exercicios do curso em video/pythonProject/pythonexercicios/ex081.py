lista = []
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
print(f'''Foram digitados {len(lista)} números na lista.\n
Em ordem decrescente os valores da lista são: {sorted(lista, reverse=True)}.\n''')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)}.')
else:
    print('O valor 5 não foi diditado na lista!')
