import random

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")
aluno = [a1, a2, a3, a4]
print("A ordem das apresentações será: {}".format(random.sample(aluno, k=4)))
