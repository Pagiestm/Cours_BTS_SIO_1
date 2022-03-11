moy = float (input ("Saisir la moyenne du candidat : "))
if moy >= 16 :
   mention = "très bien"
   
elif moy >= 14 :
    mention = "bien"
    
elif moy >= 12 :
    mention ="Assez bien"

elif moy >= 10 :
    mention = "Passable"

elif moy >= 8 :
    mention = "Oral"

else :
    mention = "ajournée"

print(mention)
