sexo = ' '
while sexo not in 'MF':
    sexo = input("Digite o seu sexo [M/F]: ").upper()[0].strip()
    if sexo not in 'MF':
        print("\033[1;31mERRO!\033[m")
print("Sexo Registrado.")