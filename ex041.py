from datetime import date

print("\033[7m{}CATEGORIA DE NATAÇÃO{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
anonasc = int(input("Ano de nascimento: "))
idade = date.today().year - anonasc
if idade <= 9:
    print("Categoria: \033[1;36mMIRIM")
elif 9 < idade <= 14:
    print("Categoria: \033[1;36mINFANTIL")
elif 14 < idade <= 19:
    print("Categoria: \033[1;36mJUNIOR")
elif 19 < idade <= 25:
    print("Categoria: \033[1;36mSÊNIOR")
elif idade > 25:
    print("Categoria: \033[1;36mMASTER")