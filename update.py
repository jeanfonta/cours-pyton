from random import randint

def creation_perso():
    dico_perso = {}
    liste_caracteristiques_perso = []
    perso = input("Entrez le nom de votre personnage : ")
    sexe = (input("Entrez son sexe : F/M")).lower()
    while sexe != 'f' and sexe != 'm':
        sexe = (input("Tappez 'F' pour féminin ou 'M' pour masculin : ")).lower()
    race = (input("Entrez la race de votre personnage : (humain, elfe, nain ou gnome) : ")).lower()
    while race != 'humain' and race != 'elfe' and race != 'nain' and race != 'gnome':
        race = (input("Entrez 'humain', 'elfe', 'nain' ou 'gnome' : ")).lower()
    classe = (input("Choisissez votre classe (guerrier, pretre, voleur ou magicien)\n\nGuerrier - dv10 - une attaque plus conséquente\nPretre - dv8 - une défense plus forte\nVoleur - dv6 - une attaque plus conséquente\nMagicien - dv4 - une défense plus forte\n\nChoix : ")).lower()
    while classe != 'guerrier' and classe != 'pretre' and classe != 'voleur' and classe != 'magicien':
        classe = (input("Choix : guerrier, pretre, voleur ou magicien : ")).lower()
    liste_caracteristiques_perso.append(sexe)
    liste_caracteristiques_perso.append(race)
    liste_caracteristiques_perso.append(classe)
    dico_perso[perso] = liste_caracteristiques_perso
    return dico_perso

def nouveau_dv(niveau, joueur):
    liste = []
    resultat = 0
    for k, value in dico.items():
        for j, val in dico[joueur].items():
            index = val.__len__()
    classe = str(val[index-1])
    if classe == 'guerrier':
        for i in range(niveau):
            liste.append(randint(1,10))
            resultat = sum(liste)
            return resultat
    elif classe == 'pretre':
        for i in range(niveau):
            liste.append(randint(1,8))
            resultat = sum(liste)
            return resultat
    elif classe == 'voleur':
        for i in range(niveau):
            liste.append(randint(1,6))
            resultat = sum(liste)
            return resultat
    else:
        for i in range(niveau):
            liste.append(randint(1,4))
            resultat = sum(liste)
            return resultat


def tour_jeu(joueur1, joueur2, pdv1, pdv2):
    print("*********** Level " + str(j1) + " : " + str(niveau_j1) + " --- Level " + str(j2) + " : " + str(niveau_j2) + " ***********")
    attaque_de_base = 6
    resultat = 0
    liste = []
    for k, value in dico.items():
        for j, val in dico[joueur1].items():
            index = val.__len__()
    classe1 = str(val[index-1])
    if classe1 == 'guerrier':
        for i in range(niveau_j1):
            liste.append(randint(1,4))
            resultat = sum(liste) * niveau_j1
            print(resultat)
            return resultat
    elif classe1 == 'pretre':
        attaque1 = randint(1,1)
    elif classe1 == 'voleur':
        attaque1 = randint(1,3)
    else:
        attaque1 = randint(1,1)
    for k, value in dico.items():
        for j, val in dico[joueur2].items():
            index = val.__len__()
    classe2 = str(val[index-1])
    if classe2 == 'guerrier':
        defense2 = randint(1,1)
    elif classe2 == 'pretre':
        defense2 = randint(1,2)
    elif classe2 == 'voleur':
        defense2 = randint(1,1)
    else:
        defense2 = randint(1,2)
    if (resultat - defense2) < 0:
        print(str(j1) + " attaque" + " (" + str(resultat) + ") " + str(j2) + " qui se defend (" + str(defense2) + ") -->  " + str(j2) + " perd " + str(0) + " pdv ")
    else:
        print(str(j1) + " attaque" + " ("+ str(resultat) + ") " + str(j2) + " qui se defend (" + str(defense2) + ") -->  " + str(j2) + " perd " + str((resultat - defense2)) + " pdv ")
    pdv_perso2 = pdv2 - (resultat - defense2)
    for k, value in dico.items():
        for j, val in dico[joueur2].items():
            index = val.__len__()
    classe2 = str(val[index-1])
    if classe2 == 'guerrier':
        attaque2 = randint(1,3)
    elif classe2 == 'pretre':
        attaque2 = randint(1,1)
    elif classe2 == 'voleur':
        attaque2 = randint(1,3)
    else:
        attaque2 = randint(1,1)
    for k, value in dico.items():
        for j, val in dico[joueur1].items():
            index = val.__len__()
    classe1 = str(val[index-1])
    if classe1 == 'guerrier':
        defense1 = randint(1,1)
    elif classe1 == 'pretre':
        defense1 = randint(1,2)
    elif classe1 == 'voleur':
        defense1 = randint(1,1)
    else:
        defense1 = randint(1,2)
    if (attaque2 - defense1) < 0:
        print(str(j2) + " attaque" + " (" + str(attaque2) + ") " + str(j1) + " qui se defend (" + str(defense1) + ") -->  " + str(j1) + " perd " + str(0) + " pdv ")
    else:
        print(str(j2) + " attaque" + " ("+ str(attaque2) + ") " + str(j1) + " qui se defend (" + str(defense1) + ") -->  " + str(j1) + " perd " + str((attaque2 - defense1)) + " pdv ")
    pdv_perso1 = pdv1 - (attaque2 - defense1)

    if pdv_perso1 <= 0:
        print("Partie terminée. " + str(j1) + " a perdu.")
        exit()
    if pdv_perso2 <= 0:
        print("Partie terminée. " + str(j2) + " a perdu.")
        exit()
    print("*********** Nouveaux PDV ***********")
    print("PDV " + str(j1) + " = " + str(pdv_perso1))
    print("PDV " + str(j2) + " = " + str(pdv_perso2))
    return ""


nb_persos = 0
dv_persos = [10]*2

dico = {}
choix_utilisateur = (input("Etes-vous prêt à créer votre premier personnage ? (O/N) : ")).lower()
while choix_utilisateur != 'o' and choix_utilisateur != 'n':
    choix_utilisateur = (input("Tappez 'O' pour continuer à créer ou 'N' pour commencer à jouer : ")).lower()
while choix_utilisateur == 'o':
    dico[nb_persos] = creation_perso()
    nb_persos = nb_persos + 1
    choix_utilisateur = (input("Voulez-vous créer un nouveau personnage? (O/N) : ")).lower()
    if choix_utilisateur != 'n' and choix_utilisateur != 'o':
        choix_utilisateur = (input("Tappez 'O' pour continuer à créer ou 'N' pour commencer à jouer : ")).lower()
niveau = [1] * nb_persos
if nb_persos <= 1:
    print("Vous n'avez pas assez de personnages! Recommencez.")
    exit()
#print("Voici vos différents personnages : ")
#compteur2 = 0
#for k, value in dico.items():
#    for j, val in dico[k].items():
#        print(j)
print("\nLet the game begin !")
print("--------------------------------------------------------------\n")
joueur1 = randint(0,nb_persos-1)
joueur2 = randint(0,nb_persos-1)
while joueur1 == joueur2:
    joueur1 = randint(0,nb_persos-1)
    joueur2 = randint(0,nb_persos-1)
for k, value in dico.items():
    for j, val in dico[k].items():
        if joueur1 == k:
            j1 = j
    for h, fol in dico[k].items():
        if joueur2 == k:
            j2 = j
print("Voici les deux joueurs qui vont s'affronter : " + str(j1) + " et " + str(j2) )
tour = 1
pdv_lev1 = [10] * 2

dv_persos = [10]*2
niveau_j1 = randint(1,10)
niveau_j2 = randint(1,10)

pdv_perso1 = pdv_lev1[0] + nouveau_dv(niveau_j1, joueur1)
pdv_perso2 = pdv_lev1[1] + nouveau_dv(niveau_j2, joueur2)
dv1 = dv_persos[0]
dv2 = dv_persos[1]


continuer_tour = (input("Commencer le premier tour ? (O/N) : ")).lower()
while continuer_tour != 'o' and continuer_tour != 'n':
    continuer_tour = (input("Commencer le premier tour ? (O/N) : ")).lower()
while continuer_tour == 'o':
    print(j1 + " possède : " + str(pdv_perso1) + " pdv")
    print(j2 + " possède : " + str(pdv_perso2) + " pdv")
    print("\n---------- TOUR " + str(tour) + " ----------")

    tour_jeu(joueur1, joueur2, pdv_perso1, pdv_perso2)
    continuer_tour = (input("Passer au tour suivant ? (O/N) : ")).lower()
    tour = tour + 1
    if continuer_tour != 'o' and continuer_tour != 'n':
        continuer_tour = (input("Passer au tour suivant ? (O/N) : ")).lower()
print("Vous avez arreter le jeu.")
