def contador(i, f, p):      # ao abrir aspas duplas 3x após criar uma função, abre-se o campo para adc informção
    """
    Faz a contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Higor Costa, aluno do 'Curso em Video'
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')


help(contador)      # chama o manual da fnção. Seja ela criada ou nativa
