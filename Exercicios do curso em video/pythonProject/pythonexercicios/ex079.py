num = list()
while True:
    n = int(input('Digite um valor para adicioná-lo à lista: '))
    if n not in num:
        num.append(n)
    else:
        print('Número já adicionado na lista! Digite outro ou encerre.')
    mais = input('Quer continuar? [S/N]: ')
    while mais in 'Ss':
        n = int(input('Digite um valor para adicioná-lo à lista: '))
        if n not in num:
            num.append(n)
        else:
            print('Número já adicionado na lista! Digite outro ou encerre.')
        mais = input('Quer continuar? [S/N]: ')
    while mais not in 'SsNn':
        print('Opção inválida.', end='')
        mais = input('Quer continuar? [S/N]: ')
    if mais in 'Nn':
        print('Encerrando lista...')
        break
print(f'A lista criada, em ordem crescente é: {sorted(num)}')
