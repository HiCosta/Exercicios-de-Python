print('Gerador de PA')
print('-=' * 10)
prim = int(input('Digite o primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += raz
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer mostrar?'))
print('Progressão finalizada com {} termos.'.format(total))
