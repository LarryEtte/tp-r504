def puissance(a,b):    
    if (not type(a) is int) or (not type(b) is int):
        raise TypeError("Integers only")
        exit(-1)
    if a == 0 and b <= 0:
        raise ValueError("Undefined exposant")
    res = a
    if b < 0:
        pow = -b
    else:
        pow = b
    for i in range(pow-1):
        res *= a
    if b < 0:
        res = 1/res
    print(f"Le résultat de {a} à l'exposant {b} est {res}")
    return res
