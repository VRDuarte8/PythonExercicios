aluno = {'nome': input("Nome: "), 'média': float(input("Média: "))}
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print("---"*20)
for k, v in aluno.items():
    print(f"{k} = {v}")