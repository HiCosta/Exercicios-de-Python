from math import pow
opos = int(input('Digite o valor do cateto oposto: '))
adj = int(input('Digite o valor do cateto adjascente: '))
hip = pow(opos, 2) + pow(adj, 2)
print('A hipotenusa desse triangulo é {}'.format(hip))
