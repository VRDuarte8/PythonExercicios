from math import hypot

co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
h = hypot(co, ca)
print("A hipotenusa do triângulo é {}".format(h))
