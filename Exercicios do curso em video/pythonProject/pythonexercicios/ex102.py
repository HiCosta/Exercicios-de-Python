def fatorial(num=1, show=False):        # show no padrão False, se colocado em True mostra calculo
    """
    Calculo de fatoriais mostrando ou não processo.
    :param num: numero a ser calculado seu fatorial
    :param show: se quiser mostrar processo do fatorial além do resultado
    :return: retorna valor do fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} x ', end='')
        f *= c
    return f


print(fatorial(5, True))        # True indicando que quero ver o calculo
print(fatorial(5))              # False indicando apenas resultado
