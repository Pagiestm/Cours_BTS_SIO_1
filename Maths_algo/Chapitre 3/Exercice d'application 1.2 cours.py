REM = 0
QTITE = float (input ("Veuillez entrer la quantité de produits : "))
PU = float (input ("Veuillez entrer le prix de ce produit : "))
MTHT = QTITE * PU
if MTHT > 700 :
    REM = 50
MTNET = MTHT - REM
print ("Montant net = ", MTNET)
