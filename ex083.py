parenteses = list()
expressao = input("Digite uma expressão com parênteses: ")
for c in expressao:
    if c == '(':
        parenteses.append(c)
    elif c == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(c)
            break
if len(parenteses) == 0:
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")
