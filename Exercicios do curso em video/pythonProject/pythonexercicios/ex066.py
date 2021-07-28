soma = n = num = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    num = num + 1
    soma += n
print(f'Foram digitados {num} números e a soma entre eles é {soma}.')
