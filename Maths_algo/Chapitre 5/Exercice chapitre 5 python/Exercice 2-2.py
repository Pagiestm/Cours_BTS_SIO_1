mot=str(input("Sasir un mot : "))
Nvmot=""
k=0
n=len(mot)
for i in range(n):
    if mot[i]=="a":
        k=k+1
    else:
        Nvmot=Nvmot+mot[i]
print(Nvmot,k)
