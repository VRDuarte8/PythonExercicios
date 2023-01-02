frase = input("Digite uma frase: ").upper().strip()
print("Quantidade de letras 'a': " + str(frase.count('A')))
print("Primeira posição: " + str(frase.find('A')+1))
print("Última posição: " + str(frase.rfind('A')+1))
