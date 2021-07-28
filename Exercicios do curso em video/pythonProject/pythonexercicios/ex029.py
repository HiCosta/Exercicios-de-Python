vel = int(input('Digite a velocidade que o carro está: '))
if vel > 80:
    print('Você foi multado em {} reais'.format((vel - 80) * 7))
