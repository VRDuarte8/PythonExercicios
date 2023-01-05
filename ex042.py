print("\033[7m{}ANALISADOR DE TRIÂNGULOS{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)

r1 = float(input("Valor da primeira reta: "))
r2 = float(input("Valor da segunda reta: "))
r3 = float(input("Valor da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As três retas \033[1;32mformam um triângulo ",end='')
    if r1 == r2 == r3:
        print("\033[1;32mEQUILÁTERO!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("\033[1;32mISÓSCELES!")
    else:
        print("\033[1;32mESCALENO!")
else:
    print("As três retas \033[1;31mnão formam um triângulo!")
