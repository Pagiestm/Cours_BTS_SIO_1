a=float(input("saisir la première valeur : "))
b=float(input("saisir la deuxième valeur : "))
c=float(input("saisir la troisième valeur : "))
if a<=b :
    if a<=c :
        min = a
    else :
        min = c
else :
    if b<=c :
        min = b
    else :
        min = c
print(min)
