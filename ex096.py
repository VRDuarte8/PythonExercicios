def area(lar, com):
    a = lar*com
    print(f"A área de um terreno de {lar}x{com} é de {a}m2.")


print(" Controle de Terrenos")
print("--"*20)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)
