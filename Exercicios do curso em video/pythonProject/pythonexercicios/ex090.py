aluno = dict()
aluno['Nome'] = str(input('Nome do aluno(a): '))
aluno['Média'] = float(input('Média do aluno(a): '))
aluno['Situação'] = 'APROVADO' if aluno['Média'] > 7 else 'REPROVADO'
print(aluno)
