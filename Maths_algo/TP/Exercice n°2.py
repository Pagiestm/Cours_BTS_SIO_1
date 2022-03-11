from math import *
a=float(input("saisir a : "))
b=float(input("saisir b : "))
c=float(input("saisir c : "))
delta=b**2-4*a*c
if delta<0 :
    print ("L'équation du second degré n'a pas de la solution dans R")
else :
    sol1=(-b-sqrt(delta))/(2*a)
    sol2=(-b+sqrt(delta))/(2*a)
    print(sol1,sol2)


