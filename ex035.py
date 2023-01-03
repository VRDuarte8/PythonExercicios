print("            Analisador de Triângulos           ")
print('----' * 20)

r1 = float(input("Valor da primeira reta: "))
r2 = float(input("Valor da segunda reta: "))
r3 = float(input("Valor da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As três retas formam um triângulo!")
else:
    print("As três retas não formam um triângulo!")
