galera = list()
dado = list()
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    cont = str(input('Quer continuar? [S/N]: '))
    if cont in 'Nn':
        print('Encerrando lista...')
        break
print(f'{len(galera)} pessoas foram cadastradas na lista.')
print(f'O maior peso foi {mai} KG. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {men} KG. Peso de ', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()
