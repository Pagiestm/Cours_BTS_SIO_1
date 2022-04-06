Tab=[[0 for l in range(4)]for c in range(4)]
k=0
for l in range(4):
    for c in range (4):
        Tab[l][c]=k+1
        k=k+1
    print(Tab[l])
