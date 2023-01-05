from math import pow

print("\033[7m{}CÁLCULO IMC{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
peso = float(input("Peso: "))
altura = float(input("Altura (em metros): "))
imc = peso / pow(altura, 2)
print("IMC: {:.2f}".format(imc))
if imc < 18.5:
    print("\033[1;32mABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("\033[1;34mPESO IDEAL")
elif 25 <= imc < 30:
    print("\033[1;32mSOBREPESO")
elif 30 <= imc < 40:
    print("\033[1;33mOBESIDADE")
elif imc >= 40:
    print("\033[1;31mOBESIDADE MÓRBIDA")
