Cote = float(input("Entrer côte de l'étudient svp : "))
Cote = round(Cote)

if Cote in range(1, 21):
    if Cote <= 9:
        print("échec")
    elif Cote <= 11:
        print("réussi sans mention")
    elif Cote <= 13:
        print("reussi avec satisfation")
    elif Cote <= 15:
        print("reussis avec distinction")
    elif Cote <= 17:
        print("reussis avec grand distinction")
    elif Cote <= 20:
        print("reussis avec la plus grande distinction")
else:
    print("mauvaise entrée")
