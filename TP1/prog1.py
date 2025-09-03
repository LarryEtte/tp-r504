import fonctions as f

print("Hello, World!")

a=float(input("Choisissez un nombre: "))
b=float(input("Choisissez un exposant: "))

res = f.puissance(a,b)

while True:
    a = float(input("Choisissez un nombre: "))
    res = a ** 2
    print (f"Le carré de {a} est {res}")
