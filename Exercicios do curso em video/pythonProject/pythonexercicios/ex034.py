sal = float(input('Qual o salário atual do funcionário? R$ '))
aum1 = (10 * sal) / 100
aum2 = (15 * sal) / 100
if sal >= 1250:
    print('O salário com aumento subirá para R${:.2f} '.format(sal + aum1))
else:
    print('O salário com aumento subirá para R${:.2f}'.format(sal + aum2))
