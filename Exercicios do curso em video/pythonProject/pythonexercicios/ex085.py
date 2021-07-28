total = [[], []]
valor = 0
for v in range(0, 7):
    valor = int(input('Digite o valor: '))
    if valor % 2 == 0:
        total[0].append(valor)
    else:
        total[1].append(valor)
total[0].sort()
total[1].sort()
print(f'Os valores pares foram {total[0]} e os ímpares foram {total[1]}.')
