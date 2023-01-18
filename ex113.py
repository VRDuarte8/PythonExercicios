def leiaInt(f):
    while True:
        try:
            num = int(input(f))
        except (ValueError, TypeError):
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print("\033[1;31mERRO! O número não foi digitado.\033[m")
            return 0
        except:
            print("\033[1;31mERRO!\033[m")
        else:
            break
    return num


def leiaFloat(f):
    while True:
        try:
            num = float(input(f))
        except ValueError:
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print("\033[1;31mERRO! O número não foi digitado.\033[m")
            return 0
        except:
            print("\033[1;31mERRO!\033[m")
        else:
            break
    return num


i = leiaInt("Digite um número inteiro: ")
r = leiaFloat("Digite um número real: ")
print(f"Você digitou o número inteiro {i} e o real {r}")
