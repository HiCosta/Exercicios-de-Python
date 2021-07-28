def ficha(jog='<Desconhecido>', gol=0):
    """
    Ficha de jogadores e seus gols
    :param jog: nome do jogador
    :param gol: gols feitos
    :return:
    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():       # verificando se é numerico
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
