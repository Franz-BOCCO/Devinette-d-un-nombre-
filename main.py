def hazard ():
    import random as rd 
    return rd.randint(1, 101)
a=hazard()
b=""
D=10
print ("DEVINEZ UNE VALEUR COMPRISE ENTRE 1 ET 101")
for j in range (10):
    D-=1
    if D==0:
        print (f"**VOUS AVEZ PERDU**     CHANCE RESTANTES=0 \n LA VALEUR A TROUVER EST {a}")
        break  
    b=int (input ("ENTREZ VOTRE VALUER : ")) 
    if b== a :
        print (f"**VOUS AVEZE GAGNEZ**     CHANCES RESTANTES : {D}") 
        break
    elif b<a :
        print (f"{b} EST INFERIEUR     CHANCES RESTANTES : {D}")
        continue
    elif b>a  :
        print (f"{b} EST SUPERIEUR     CHANCES RESTANTES : {D}")
        continue     