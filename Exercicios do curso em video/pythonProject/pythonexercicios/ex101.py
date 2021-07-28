def voto(ano=1):
    from datetime import datetime       # dessa forma a biblioteca so é importada dentro dessa função.
    global idade
    idade = datetime.now().year - ano
    return idade


idade = int(input('Digite o ano do seu nascimento: '))
if voto(idade) < 16:
    print(f'Com {idade} anos: NÃO VOTA')
elif 18 > idade > 16 or idade > 85:
    print(f'Com {idade} anos: VOTO OPCIONAL')
else:
    print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
