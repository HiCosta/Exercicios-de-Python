print('Gerador de PA')
print('-=' * 10)
prim = int(input('Digite o primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = prim
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += raz
    cont += 1
print('Fim')
