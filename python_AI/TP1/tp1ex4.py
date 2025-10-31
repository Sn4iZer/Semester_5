import math

a = int(input("Entre a : "))
b = int(input("Entre b : "))
c = int(input("Entre c : "))

delta = (b*b)-(4*a*c)

if (delta > 0):
    x1 = ((-b) + math.sqrt(delta))/(2*a)
    x2 = ((-b) - math.sqrt(delta))/(2*a)
    print("Premier resultat : X1 = ", x1)
    print("Deuxieme resultat : X2 = ", x2)

elif(delta == 0):
    x1 = (-b)/(2*a)
    print("Resultat X = ", x1)
else:
    print("Resulat admit un nombre complixe.")
