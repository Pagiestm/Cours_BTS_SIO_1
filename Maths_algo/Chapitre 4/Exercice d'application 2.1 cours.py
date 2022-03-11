premterm = int(input("Saisir un premterm : "))
nbterm = int(input("Saisir nbterm : "))
r = int(input("Saisir r : "))
terme = premterm
for compteur in range(1,nbterm+1):
    terme = terme + r
    print(terme)

