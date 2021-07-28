def linha():        # define uma função
    print('-=' * 20)


linha()     # função criada previamente
print('Hello, world!')
linha()


def titulo(txt):        # criando função tipo texto
    print(txt)


titulo('Testando função')   # acionando função
linha()


def soma(a, b):     # função criada para somar dois numeros e mostrar o resultado
    s = a + b
    print(s)


titulo('Testando com operadores')
linha()
soma(10, 5)
soma(200, 568)


def contador(* num):     # função criada para empacotamento(quant de numeros da função vai depender do usuário)
    print(num)


linha()
contador(1, 2, 3, 4)        # tupla criada em função
contador(1, 2)
contador(5, 6, 7, 8, 9, 0, 1, 2, 3)
linha()
linha()


def dobra(lista):       # função criada para dobrar os valores em uma lista
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4]      # valores antes de dobrar
dobra(valores)
print(valores)          # valores dobrados
print(valores[3])
