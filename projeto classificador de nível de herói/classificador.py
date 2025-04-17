nome = str(input("digite o nome do seu herói:"))

xp = float(input("digite o xp do seu herói:"))


if xp < 1000:
    print(f"O héroi de nome {nome} está no nível de prata")
elif xp >= 1001 and xp <= 2000:
    print(f"O héroi de nome {nome} está no nível de bronze")
elif xp >= 2001 and xp <= 5000:
    print(f"O héroi de nome {nome} está no nível de ouro")
elif xp >= 6001 and xp <= 7000:
    print(f"O héroi de nome {nome} está no nível de platina")
elif xp >= 7001 and xp <= 8000:
    print(f"O héroi de nome {nome} está no nível de ascendente")
elif xp >= 8001 and xp <= 9000:
    print(f"O héroi de nome {nome} está no nível de imortal")
elif xp >= 9001 and xp <= 10000:
    print(f"O héroi de nome {nome} está no nível de radiante")
elif xp >= 10001:
    print(f"O héroi de nome {nome} está no nível de expert")
else:
    print("valor incorreto")


