from time import sleep

print("\033[7m{}CONVERSOR DE NÚMEROS{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
n = int(input("Digite um número: "))
calculo = input("Escolha a conversão que deseja realizar:\n[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal\n\n")
if calculo == '1':
    print("Número convertido em binário: {}".format(bin(n)[2:]))
elif calculo == '2':
    print("Número convertido em octal: {}".format(oct(n)[2:]))
elif calculo == '3':
    print("Número convertido em hexadecimal: {}".format(hex(n))[2:])
else:
    print("\033[31mERRO")
    print("Escolha um cálculo válido")