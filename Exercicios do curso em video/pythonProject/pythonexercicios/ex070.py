soma = maismil = menor = cont = 0
barato = ''
nome = str(input('Nome do produto: '))
preco = float(input('Preço do produto: R$ '))
cont += 1
prod = str(input('Quer adicionar mais produtos? [S/N]: '))
soma += preco
if preco > 1000:
    maismil += 1
if cont == 1 or preco < menor:
    menor = preco
    barato = nome
while prod in 'Ss':
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    cont += 1
    prod = str(input('Quer adicionar mais produtos? [S/N]: '))
    if preco < preco:
        barato = nome
    soma += preco
    if preco > 1000:
        maismil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if prod in 'Nn':
        break
print(f'Gasto total: {soma:.2f}\n {maismil} produtos custam mais de mil reais\n O produto mais barato foi: {barato}')
