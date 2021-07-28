preco = float(input('Valor do produto em R$: '))
pg = int(input('''Escolha sua forma de pagamento:\n 1- À vista dinheiro/cheque (10% desconto)
 2- À vista cartão (5% desconto)\n 3- Em até 2x cartão\n 4- 3x ou mais cartão (20% juros): '''))
if pg == 1:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco - (preco * 10 / 100)))
if pg == 2:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco - (preco * 5 / 100)))
if pg == 3:
    print('O valor a ser pago são 2x de R$ {:.2f}'.format(preco / 2))
if pg == 4:
    print('O valor a ser pago são 3x de R$ {:.2f}'.format((preco + (preco * 20 / 100)) / 3))
