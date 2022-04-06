mot=str(input("Saisir un mot : "))
b=0
n=len(mot)
a=""
for i in range(n):
    if mot[i]=="a":
        a=a+"%"
        b=b+1
    else:
        a=a+mot[i]
print(a,b)
