import fonctions as f

print("Hello, World!")

a=5
b=4.2

res = f.puissance(a,b)

while True:
    a = float(input("Choisissez un nombre: "))
    res = a ** 2
    print (f"Le carré de {a} est {res}")
