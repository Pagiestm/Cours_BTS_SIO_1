prenom = str (input ("Saisir votre pénom : "))
nom = str (input ("Saisir votre nom : "))
sexe = str (input ("Saisir F pour femme et G pour homme : "))
if sexe == "F" :
    print ("Bonjour Madame" , nom , prenom)
else :
    print ("Bonjour Monsieur" , nom , prenom)
