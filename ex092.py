from datetime import datetime

pessoa = {'Nome': input('Nome: '), 'idade': datetime.now().year - int(input('Ano de nascimento: ')),
          'Carteira de trabalho': int(input('Carteira de trabalho: '))}

if pessoa['Carteira de trabalho'] > 0:
    pessoa['Ano de contratação'] = int(input("Ano de contratação: "))
    pessoa['Salário'] = float(input("Salário: "))
    pessoa['Idade de aposentadoria'] = pessoa['idade'] + ((pessoa['Ano de contratação'] + 35) -
                                                          datetime.now().year)

print("---" * 20)
for k, v in pessoa.items():
    print(f"- {k} é {v}")
