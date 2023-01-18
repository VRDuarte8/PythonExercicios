def aumentar(m, a, form=False):
    """
    -> Aumenta valores
    :param m: valor inicial
    :param a: taxa de aumento
    :param form: formatação monetária
    :return: valor aumentado
    """
    m = m * (a / 100 + 1)
    if form:
        return f"R${m:.2f}"
    else:
        return m


def diminuir(m, d, form=False):
    """
    -> Reduz valores
    :param m: valor inicial
    :param a: taxa de redução
    :param form: formatação monetária
    :return: valor reduzido
    """
    m = m * ((100 - d)/100)
    if form:
        return f"R${m:.2f}"
    else:
        return m


def dobro(m, form=False):
    """
    -> Dobra valores
    :param m: valor inicial
    :param form: formatação monetária
    :return: valor dobrado
    """
    m = m * 2
    if form:
        return f"R${m:.2f}"
    else:
        return m


def metade(m, form=False):
    """
    -> Divide valores pela metade
    :param m: valor inicial
    :param form: formatação monetária
    :return: valor dividido
    """
    m = m / 2
    if form:
        return f"R${m:.2f}"
    else:
        return m


def resumo(m, a, d):
    """
    -> Mostra tabela com análise de valores
    :param m: valor analisado
    :param a: taxa de aumento
    :param d: taxa de redução
    :return: tabela
    """
    tit = "RESUMO DO VALOR"
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print('Preço analisado: \tR${m:.2f}')
    print('Dobro do preço: \t{dobro(m, True)}')
    print('Metade do preço: \t{metade(m, True)}')
    print(f'{a}% de aumento: \t {aumentar(m, a, True)}')
    print(f'{d}% de redução: \t{diminuir(m, d, True)}')
    print('-' * 30)
