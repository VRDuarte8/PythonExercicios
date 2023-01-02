cidade = input("Digite o nome de uma cidade: ").strip().upper()
print("Ela começa com 'Santo'? " + str('SANTO' in cidade[:cidade.find(" ")]))
