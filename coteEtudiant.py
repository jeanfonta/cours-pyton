import math


def coteEtudiant(cote):
    if cote <= 9:
        print("l'etudiant est en échec")
    elif cote <= 11:
        print("l'étudiant a réussi sens mention")
    elif cote <= 13:
        print("l'étudiant a réussi avec satisfaction")
    elif cote <= 15:
        print("l'étudiant a réussi avec distinction")
    elif cote <= 20:
        print("l'étudiant a réussi avec la plus grande distinction")
    else:
        cote = float(input("entree une cote comprise entre 0 et 20 svp"))
    return cote


def programme():
    cote = float(input("entree votre cote entre 0 et 20 svp"))
    cote = round(cote)
    coteEtudiant(cote)


programme()
