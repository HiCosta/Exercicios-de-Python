num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opc = int(input('Digite sua opção: '))
if opc == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
