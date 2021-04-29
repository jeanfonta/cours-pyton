fichier=open("livres.csv", "r")
contenuLivre = fichier.readlines()
fichier.close()

donneAuteurTitre = []
"""from random import randint
motMagiques = ["un peu", "passionément", "à la folie"]
motMagique = "Je t'aime " + motMagiques[randint(0, 2)]
while input("Quel est le mot magique ?") != motMagique:
    print("Tu n'as pas dit le mot magique")"""

def titreAuteur():
    for donneTab in contenuLivre:
        donneTab = donneTab.split('#')
        if donneTab[2] == "Margaret Weis & Tracy Hickman":
            ###temp = [donneTab[1],donneTab[2]]
            """temp.append(donneTab[1])
            temp.append(donneTab[2])"""
            donneAuteurTitre.append([donneTab[1],donneTab[2]])

titreAuteur()


def aficherDonne():
    for liste in donneAuteurTitre:

        print("titre :", liste[0], "\nauteur :", liste[1])
    print("nombre de livre de ", donneAuteurTitre[0][1], " :", len(donneAuteurTitre))

aficherDonne()


donneEditeur = []


def editeur():
    for donneTab in contenuLivre:
        donneTab = donneTab.split('#')
        insertionOk = True
        for editeur in donneEditeur:
            if donneTab[3].upper() == editeur.upper():
                insertionOk = False

        if insertionOk :
            donneEditeur.append(donneTab[3])

editeur()


def afficherEditeur():
    for liste in donneEditeur:
        print("l'editeur est :", liste)
    ###print("l'editeur est : ", donneEditeur, "\nle nombre d'editeur est :",len(donneEditeur))
afficherEditeur()
print(len(donneEditeur))

titreEtAnnee = []


