print("\033[7m{}PALÍNDROMO{}\033[m".format(" " * 20, " " * 20))
print("---" * 20)
frase = input("Digite a frase: ").strip().upper().replace(" ", "")
palindromo = 0
for c in range(0, len(frase)):
    if frase[c] != frase[len(frase) - 1 - c]:
        palindromo = 1
if palindromo == 0:
    print("É um palindromo")
else:
    print("Não é um palíndromo")