print("\033[7m{}APROVAÇÃO{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print("Média final: {}".format(media))
if media < 5:
    print("\033[1;31mREPROVADO")
elif 5 <= media < 6.9:
    print("\033[1;33mRECUPERAÇÃO")
elif media >= 7:
    print("\033[1;34mAPROVADO")
