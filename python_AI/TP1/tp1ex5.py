N = input("Entre 3 number : ")

a = int(N[0])
b = int(N[1])
c = int(N[2])

n1 = a*100 + b*10 + c
n2 = a*100 + c*10 + b
n3 = b*100 + a*10 + c
n4 = b*100 + c*10 + a
n5 = c*100 + a*10 + b
n6 = c*100 + b*10 + a

print("Les Nombres fornes par les chiffres N sont : ", n1,", " ,n2,", " , n3 ,", " , n4 ,", " ,n5,", " , n6)