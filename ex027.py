nome = input("Digite um nome completo: ")
nome = nome.strip()
print("Primeiro nome: " + nome[:nome.find(" ")])
print("Último nome: " + nome[nome.rfind(" ") + 1:])
