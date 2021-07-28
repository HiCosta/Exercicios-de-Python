idade = int(input('Qual a sua idade? '))
sexo = str(input('Qual o seu sexo [M/F]: '))
pes = str(input('Quer adicionar mais pessoas [S/N]? '))
mais18 = 0
homens = 0
mu_18 = 0
if idade > 18:
    mais18 += 1
if sexo in 'Mm':
    homens += 1
if sexo in 'Ff' and idade < 18:
    mu_18 += 1
while pes in 'Ss':
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo [M/F]: '))
    pes = str(input('Quer adicionar mais pessoas [S/N]? '))
    if idade > 18:
        mais18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 18:
        mu_18 += 1
    if pes in 'Nn':
        break
print(f'Ao todo {mais18} tem mais de 18 anos, {homens} homens foram cadastrados, {mu_18} mulheres tem menos de 18 anos')
