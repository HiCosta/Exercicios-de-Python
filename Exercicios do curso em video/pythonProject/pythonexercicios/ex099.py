def maior(* num):
    cont = maior = 0
    print('Analisando os valores ...')
    for valor in num:
        print(f'{valor}', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')


maior(1, 2, 5, 9, 4, 3, 11, 20)
