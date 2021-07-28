lista = []
for v in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} e ele esta na posição: {lista.index(maior)}, o menor valor foi {menor}'
      f' e ele esta na posição: {lista.index(menor)}.')
