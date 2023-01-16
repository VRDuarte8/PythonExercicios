def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários aluno.
    :param notas: uma ou mais notas dos aluno (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    info = dict()
    media = sum(notas) / len(notas)
    info['Quantidade de notas'] = len(notas)
    info['Maior nota'] = max(notas)
    info['Menor nota'] = min(notas)
    info['Média da turma'] = media
    if sit:
        if media >= 7:
            info['Situação'] = 'BOA'
        elif 5 <= media < 7:
            info['Situação'] = 'RAZOÁVEL'
        elif media < 5:
            info['Situação'] = 'RUIM'
    return info


resp = notas(4, 3, 5, 2, 0, sit=True)
print(resp)
#help(notas)