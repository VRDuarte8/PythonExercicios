distancia = float(input("Qual a distância que será percorrida na viagem? "))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print("O preço da passagem será de R${:.2f}".format(preco))
