n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opc = 0
while opc != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opc = int(input('Digite sua opção: '))
    if opc == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    if opc == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    if opc == 3:
        if n1 > n2:
            print('O número maior é o {}.'.format(n1))
        elif n1 < n2:
            print('O número maior é o {}.'.format(n2))
    if opc == 4:
        opc = int(input('Digite sua opção novamente: '))
    if opc == 5:
        print('Programa encerrado!')
