from random import randint

tab1 =["je t'aime","je t'adore","je t'apprécie"]
tab2 =["baucoups","passionnément","a la follie"]

for i in range(0,5):
    aleatoirTab1 = randint(0,len(tab1))-1
    aleatoireTab2 = randint(0,len(tab2))-1
    print(tab1[aleatoirTab1],tab2[aleatoireTab2])
