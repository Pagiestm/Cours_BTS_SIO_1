a=float(input("saisir la première valeur : "))
b=float(input("saisir la deuxième valeur : "))
c=float(input("saisir la troisième valeur : "))
if a>=b :
    if a>=c :
        max = a
    else :
        max = c
else :
    if b>=c :
        max = b
    else :
        max = c
print(max)
