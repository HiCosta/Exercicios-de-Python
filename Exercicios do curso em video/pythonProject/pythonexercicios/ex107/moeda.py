def aumentar(preco, taxa):
    """
    Aumenta valor em preço de produto
    :param preco: preço atual
    :param taxa: valor a ser adicionado ao preco atual
    :return: retorna valor atualizado
    """
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco, taxa):
    """
    Diminuir valor em preço de produto
    :param preco: preço atual
    :param taxa: valor a ser subtraido do preço atual
    :return: retorna valor atualizado
    """
    res = preco - (preco * taxa / 100)
    return res


def dobrar(preco):
    """
    Dobrar valor do preço atual de um produto
    :param preco: preço atual
    :return: retorna valor atualizado
    """
    res = preco * 2
    return res


def metade(preco):
    """
    Cortar pela metade preço atual do produto
    :param preco: preço atual
    :return: retorna valor atualizado
    """
    res = preco / 2
    return res
