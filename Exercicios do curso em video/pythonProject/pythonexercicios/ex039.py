import datetime
ano = int(input('Informe o ano do seu nascimento: '))
atual = datetime.date.today().year
idade = atual - ano
if atual - ano < 18:
    print('Você ainda irá se alistar no serviço militar. Faltam {} anos.'.format(18 - idade))
elif atual - ano == 18:
    print('Já está na hora de você se alistar para o serviço militar!')
else:
    print('Você já devia ter se alistado no serviço militar. Se passaram {} anos.'.format(idade - 18))
