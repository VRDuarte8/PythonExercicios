def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    """
    result = 1
    print(f"{n}! = ", end='')
    while n >= 1:
        result *= n
        if show:
            print(n, end='')
            if n > 1:
                print(' X ', end='')
            else:
                print(' = ', end = '')
        n -= 1
    return result


num = int(input("Digite o número que deseja calcular o fatorial: "))
print(fatorial(num, True))
#help(fatorial)