print("Saisir le prix hors taxe")
prixHT=float(input())
print("Saisir le taux de TVA")
tauxdeTVA=float(input())
TVA=tauxdeTVA/100*prixHT
print("la TVA est de",TVA)
