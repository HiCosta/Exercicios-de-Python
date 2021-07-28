from random import randint
poi = str(input('Par ou Ímpar [P/I] ? ')).strip().lower()
n = int(input('Escolha um número [1 a 10]: '))
comp = randint(0, 10)
print(f'Eu escolhi {comp}')
soma = n + comp
total = 0
while soma % 2 == 0:
    if poi in 'p':
        print('Você ganhou!')
        print('-=' * 17)
        total += 1
        poi = str(input('Par ou Ímpar [P/I] ? ')).strip().lower()
        n = int(input('Escolha um número [1 a 10]: '))
        print('-=' * 17)
    if poi in 'i':
        print('Você perdeu!')
        break
while soma % 2 != 0:
    if poi in 'i':
        print('Você ganhou!')
        total += 1
        poi = str(input('Par ou Ímpar [P/I] ? ')).strip().lower()
        n = int(input('Escolha um número [1 a 10]: '))
        print('-=' * 17)
    if poi in 'p':
        print('Você perdeu!')
        break
print(f'Você ganhou {total} vezes consecutivas!')
