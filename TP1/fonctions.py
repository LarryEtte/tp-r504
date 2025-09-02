def puissance(a,b):    
    if (not type(a) or (not type(b))):
        raise TypeError("Integers only")
        exit()
    res = a ** b
    print(f"Le résultat de {a} à l'exposant {b} est {res}")
    return res
