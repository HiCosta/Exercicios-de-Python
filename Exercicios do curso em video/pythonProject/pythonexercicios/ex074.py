from random import randint
n1 = randint(1, 6)
n2 = randint(1, 6)
n3 = randint(1, 6)
n4 = randint(1, 6)
n5 = randint(1, 6)
tupla = n1, n2, n3, n4, n5
print(f'Os valores sorteados foram:', tupla)
print('O menor número sorteado foi o número: ', min(tupla))
print('O maior número listado foi o número: ', max(tupla))
