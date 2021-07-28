casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos quer pagar a casa? '))
parcela = casa / (anos * 12)
if parcela > (30 * salario / 100):
    print('Infelizmente você não poderá financiar essa casa, sinto muito!')
else:
    print('Você financiará essa casa em {} parcelas de R${:.2f}'.format(anos, parcela))
