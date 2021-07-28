def soma(a, b, c=0):
    s = a + b + c
    return s        # função que retorna para valor para s, podendo ser usado em mais variaveis


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(5, 0)
print(f'Os resultados foram {r1}, {r2} e {r3}.')
print('-=-' * 20)


def fatorial(num=1):        # o '=0' significa que se não passar valor nenhum, este será 0
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
