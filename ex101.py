def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade <= 70:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."
    elif 16 <= idade < 18 or idade > 70:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO NEGADO"


a = int(input("Em que ano você nasceu? "))
print(voto(a))
