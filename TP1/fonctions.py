def puissance(a,b):
    if (not type(a) is int) or (not type(b) is int):
        raise TypeError("Integers only")
        exit()
    res = a ** b
    print(f"Le résultat de {a} à l'exposant {b} est {res}")
    return res
