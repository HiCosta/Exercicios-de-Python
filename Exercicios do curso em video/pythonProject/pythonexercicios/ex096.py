def area(a, b):
    terreno = (a * b)
    print(f'A área de um terremo com {a} de largura e {b} de comprimento é {terreno} m².')


larg = float(input('Insira a largura do seu terreno em metros: '))
comp = float(input('Insira o comprimento do seu terreno em metros: '))
area(larg, comp)
