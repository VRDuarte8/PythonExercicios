def aumentar(m, a, form=False):
    m = m * (a / 100 + 1)
    if form:
        return f"R${m:.2f}"
    else:
        return m


def diminuir(m, d, form=False):
    m = m * ((100 - d)/100)
    if form:
        return f"R${m:.2f}"
    else:
        return m


def dobro(m, form=False):
    m = m * 2
    if form:
        return f"R${m:.2f}"
    else:
        return m


def metade(m, form=False):
    m = m / 2
    if form:
        return f"R${m:.2f}"
    else:
        return m


def resumo(m, a, d):
    tit = "RESUMO DO VALOR"
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f"{'Preço analisado:':<20}R${m:.2f}")
    print(f"{'Dobro do preço:':<20}{dobro(m, True)}")
    print(f"{'Metade do preço:':<20}{metade(m, True)}")
    print(f"{f'{a}% de aumento:':<20}{aumentar(m, a, True)}")
    print(f"{f'{d}% de redução:':<20}{diminuir(m, d, True)}")
    print('-' * 30)