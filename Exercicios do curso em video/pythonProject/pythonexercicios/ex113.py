def leiaint(msg):
    while True:
        try:        # função para tratamento de excessoes e erros
            n = int(input(msg))
        except (ValueError, TypeError):     # se for esses erros, ele retorna uma msg
            print('ERRO: por favor, digite um número inteiro válido.')
            continue        # continua tentando rodar o programa, joga direto pro while nesse caso
        else:       # se não der problema:
            return n        # retorna pra n finalizando programa


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
