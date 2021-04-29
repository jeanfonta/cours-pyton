from random import randint


def choixRace():
    race = ["Humain", "Elfe", "Nain", "Gnome"]
    saisie = -1
    while not saisieOk(saisie, len(race)):
        saisie = int(input("choix de votre race 0=Humain, 1=Elfe, 2=Nain, 3=Gnome svp : "))
    choix = race[saisie]
    return choix


def saisieOk(saisie, tailleListe):
    return saisie >= 0 and saisie < tailleListe


def choixSexe():
    sexe = ["homme", "femme", "autre"]
    saisie = -1
    while not saisieOk(saisie, len(sexe)):
        saisie = int(input("choix de votre sex 0=homme, 1=femme, 2=autre svp : "))
    choix = sexe[saisie]
    return choix


def choixDeLaClasse():
    classe = ["guerrier", "pretre", "voleur", "magicien"]
    saisie = -1
    while not saisieOk(saisie, len(classe)):
        saisie = int(input("choix de votre classe 0=guerrier, 1=pretre, 2=voleur, 3magicien"))
    choix = classe[saisie]
    return choix


def choixNom():
    nomPersonnage = input("entree votre nom de personnage svp :")
    return nomPersonnage


def creationPersonnage():
    personnage = {}
    personnage["race"] = choixRace()
    personnage["sexe"] = choixSexe()
    personnage["classe"] = choixDeLaClasse()
    personnage["nom"] = choixNom()
    personnage["attaque"] = randint(6, 10)
    personnage["defence"] = randint(1, 5)
    personnage["niveaux"] = randint(1, 10)
    personnage["vie"] = vieParNiveau(personnage["niveaux"], personnage["classe"])
    return personnage


def vieParNiveau(niveaux, classe):
    vie = 10
    for niveau in range(2, niveaux + 1):
        vie = vie + choixDeVie(classe)

    return vie


def choixDeVie(classe):
    valeur = 0
    if classe == "guerrier":
        valeur = randint(1, 10)
    if classe == "pretre":
        valeur = randint(1, 8)
    if classe == "voleur":
        valeur = randint(1, 6)
    if classe == "magicien":
        valeur = randint(1, 4)
    return valeur


def selectionPersonnage(listePersonnage):
    personnageCombat = []
    if len(listePersonnage) >= 2:
        for perso in range(0, 2):
            persoEnCombat = randint(0, len(listePersonnage) - 1)
            personnageCombat.append(listePersonnage[persoEnCombat])
            del listePersonnage[persoEnCombat:persoEnCombat]
    return personnageCombat


def combat(personnageCombat):
    """
    blblu
    :param personnageCombat:
    :return:
    """
    if len(personnageCombat) > 0:
        ordrePrioritaire = randint(0, len(personnageCombat) - 1)
        # tire le même personnage
        personnagePrioritaire = personnageCombat[ordrePrioritaire]
        # del personnageCombat[ordrePrioritaire:ordrePrioritaire]
        personnageCombat.pop(ordrePrioritaire)
        personnageSecondaire = personnageCombat[0]
        del personnageCombat[0:0]
        while personnagePrioritaire["vie"] > 0 and personnageSecondaire["vie"] > 0:
            degatFait = personnagePrioritaire["attaque"] - personnageSecondaire["defence"]
            personnageSecondaire["vie"] = personnageSecondaire["vie"] - degatFait
            if personnageSecondaire["vie"] <= 0:
                return personnagePrioritaire
            degatFait = personnageSecondaire["attaque"] - personnagePrioritaire["defence"]
            personnagePrioritaire["vie"] = personnagePrioritaire["vie"] - degatFait
            if personnagePrioritaire["vie"] <= 0:
                return personnageSecondaire
    return


def programme():
    listePersonnage = []
    choixUtilisateur = ""
    while len(listePersonnage) < 2 or choixUtilisateur == "y":
        listePersonnage.append(creationPersonnage())
        if len(listePersonnage) >= 2:
            choixUtilisateur = ""
            while choixUtilisateur != "y" and choixUtilisateur != "q":
                choixUtilisateur = input(
                    "voulez vous créer un nouveau personnage si oui presser y si vous voulez quitter presser q :")
    for personnage in listePersonnage:
        print(personnage)
    while len(listePersonnage) >= 2:
        listePersonnage.append(combat(selectionPersonnage(listePersonnage)))
        print("bravo vous avez gagné : ", listePersonnage[0])
    return


programme()
