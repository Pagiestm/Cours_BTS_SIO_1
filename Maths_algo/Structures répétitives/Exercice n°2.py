n=0
A=float(input("Saisir la valeur initial : "))
C=float(input("Saisir le facteur : "))
M=float(input("Saisir le seuil : "))
val=A
while val<M:
    val=C*val
    n=n+1
print (n)
