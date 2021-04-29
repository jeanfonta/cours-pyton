from random import randint


def choixDeLaRace(choixDeRace):
    if choixDeRace == 1:
        print("vous avez choisi les humains")
    elif choixDeRace == 2:
        print("vous avez choisi les nains ")
    elif choixDeRace == 3:
        print("vous avez choisi les elfes")
    elif choixDeRace == 4:
        print("vous avez choisi les ogres")
    else:
        print("le choix n'est pas valide ")


def choixDeRace2(choixRace2):
    if choixRace2 == 1:
        print("vous avez choisi d'etre humains")
    elif choixRace2 == 2:
        print("vous avez choisis d'etre un nains")
    elif choixRace2 == 3:
        print("vous avez choisis d'etre un elfes")
    elif choixRace2 == 4:
        print("vous avez chooisis d'etre un ogres")
    else:
        print("le choix n'est pas valide ")


def choixDeClasse2(choixClasse2):
    if choixClasse2 == 1:
        print("vous avez choisis d'etre un voleur")
    elif choixClasse2 == 2:
        print("vous avez choisis d'etre un mage")
    elif choixClasse2 == 3:
        print("vous avez choisis d'etre un paladin")
    elif choixClasse2 == 4:
        print("vous avez choisis d'etre un pretre")
    elif choixClasse2 == 5:
        print("vous avez choisis d'etre un necromancient")


def choixDeClasse(classeChoisie):
    if classeChoisie == 1:
        print("vous avez coisie d'etre voleur ")
    elif classeChoisie == 2:
        print("vous avez choisie d'etre un mage")
    elif classeChoisie == 3:
        print("vous voulez etre un paladin")
    elif classeChoisie == 4:
        print("bien venue pretre")
    elif classeChoisie == 5:
        print("que la mort vous acompagne necromencient ")


def nomPersonnage():
    return input("entree le nom de votre personnage svp : ")


def prenomPersonnage():
    return input("entree le prenom de votre personnage svp :")


def choixDuSex(sexPersonnage):
    if sexPersonnage == 1:
        print("vous avez choisi d'etre un homme")
    elif sexPersonnage == 2:
        print("vous avez choisi d'etre une femme")
    elif sexPersonnage == 3:
        print("vous avez choisi de ne pas vous conformer aux norme bravo ")


def choixRaceEnnemi():
    raceEnemie = ["gobelin", "salamendre", "vampire", "troll", "ouroukie", "dragons", "raptor", "t-rex"]
    return


def choixClasseEnnemi():
    classeEnemie = ["demoniste", "chamane", "destructeur", "dragoniste", "druide"]
    return


def programme():
    choixDeRace = int(input("faite votre choix \n1=humains\n2=nains\n3=elfes\n4=ogres"))
    choixRace2 = int(input("faite votre choix \n1=humains\n2=nains\n3=elfes\n4=ogres"))
    choixClasse2 = int(input("faite votres choix \n1=voleur\n2=mage\n3=paladin\n4=pretre\n5=necromancient"))
    classeChoisie = int(input("faite votre choix\n1=voleur\n2=mage\n3paladin\n4=pretre\n5=necromancient"))
    sexPersonnage = int(input("faite votre choix de sexe \n1=homme\n2=femme\n3=autre"))

    choixDeLaRace(choixDeRace)
    choixDeRace2(choixRace2)
    choixDeClasse2(choixClasse2)
    choixDeClasse(classeChoisie)
    choixDuSex(sexPersonnage)


programme()
