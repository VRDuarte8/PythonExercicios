import math

angulo = float(input("Digite o valor do ângulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print("Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(sen, cos, tg))
