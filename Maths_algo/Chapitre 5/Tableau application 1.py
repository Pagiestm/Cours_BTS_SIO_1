Tab = [0]*10
Tab [0] = float(input("Saisir la valeur de la 1ère case"))
maxi = Tab[0]
for i in range(1,10):
    Tab[i]=float(input("Saisir un nombre"))
    if Tab[i]>maxi:
        maxi=Tab[i]
print(Tab,maxi)
