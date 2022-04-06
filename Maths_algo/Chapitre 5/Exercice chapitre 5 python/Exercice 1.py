mot=str(input("Saisir un mot : "))
n=len(mot)
a=""
for i in range(n):
    if mot[i]=="a":
        a=a+"%"
    else:
        a=a+mot[i]
print(a)
