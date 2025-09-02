def puissance(a,b):    
    if (not type(a) is int) or (not type(b) is int):
        raise TypeError("Integers only")
        exit()
    if a == 0 and b <= 0:
        raise ValueError("Undefined exposant")
    res = a ** b
    print(f"Le résultat de {a} à l'exposant {b} est {res}")
    return res
