def somar(a, b, c=0):     # se colocar '= 0' após o parametro, isso o torna opcional. Caso não haja soma apenas os 2.
    """
    Função criada para somar até 3 numeros
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor

    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(2, 5)
somar(2, 5, 10)
help(somar)     # mostra manual da função
