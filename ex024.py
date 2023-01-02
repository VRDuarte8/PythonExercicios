cidade = input("Digite o nome de uma cidade: ")
print("Ela começa com 'Santo'? " + str('Santo' in cidade[:cidade.find(" ")]))
