nomUtilisateur = input("entree votre nom svp : ")


def verifiePremiereLettreNom(nom):
    '''if nom[0] == "j" or nom[0] == "n":
        print("ok")
    else:
        print("non ok")'''

    return nom[0] == "j" or nom[0] == "n"


nombreDeTour = 0

while len(nomUtilisateur) > 0 and verifiePremiereLettreNom(nomUtilisateur) is not True:
    nombreDeTour = nombreDeTour + 1
    if nombreDeTour == 5:
        break
    nomUtilisateur = input("entree votre nom svp : ")

#print(verifiePremiereLettreNom(nomUtilisateur))
