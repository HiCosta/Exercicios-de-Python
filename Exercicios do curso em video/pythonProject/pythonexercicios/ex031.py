dist = float(input('Qual a distância da viagem em Km? '))
tarif1 = 0.50
tarif2 = 0.45
if dist <= 200:
    print('A passagem será de R${:.2f}'.format(dist * tarif1))
else:
    print('A passagem será de R${:.2f}'.format(dist * tarif2))
