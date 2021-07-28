ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número para saber sua escrita por extenso [0 a 20]: '))
    if 0 <= num <= 20:
        break
    print('Opção inválida!')
print(f'Você digitou o número {ext[num]}')
