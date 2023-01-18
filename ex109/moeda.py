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