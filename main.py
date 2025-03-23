def hazard ():
    import random as rd 
    return rd.randint(1, 101)
a=hazard()
b=""
D=10
while b=="" :
    print ("DEVINEZ UNE VALEUR COMPRISE ENTRE 1 ET 101")
    break
for j in range (10):
    D-=1
    if D==0:
        break
    b=int (input ("ENTREZ VOTRE VALUER : "))
    if b== a : 
        break
    elif b<a :
        continue
    elif b>a  :
        continue     