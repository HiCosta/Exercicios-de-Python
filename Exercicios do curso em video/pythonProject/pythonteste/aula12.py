nome = str(input('Qual é o seu nome? '))
if nome == 'Higor':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Sthefany Stephanie Stefany':
    print('Belo nome!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
