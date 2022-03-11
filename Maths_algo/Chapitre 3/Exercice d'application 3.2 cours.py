CA = float(input("Saisir le chiffre d'affaire : "))
if CA < 5000 :
   Prime = 0

elif CA < 10000 :
     Prime = 5/100 * CA

elif CA < 30000 :
     Prime = 7/100 * CA
     
else :
     Prime = 0,1 *CA

print(Prime)
