def aumentar(m, a):
    m = m * (a / 100 + 1)
    return f"R${m:.2f}"


def diminuir(m, d):
    m = m * ((100 - d)/100)
    return f"R${m:.2f}"


def dobro(m):
    m = m * 2
    return f"R${m:.2f}"


def metade(m):
    m = m / 2
    return f"R${m:.2f}"