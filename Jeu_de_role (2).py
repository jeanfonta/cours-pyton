import random

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


def lance_de_classe(joueur):
    for k, value in dico.items():
        for j, val in dico[joueur].items():
            index = val.__len__()
    classe = str(val[index-1])
    if classe == 'guerrier':
        return random.randint(1,10)
    elif classe == 'pretre':
        return random.randint(1,8)
    elif classe == 'voleur':
        return random.randint(1,6)
    else:
        return random.randint(1,4)


def tour_jeu(joueur1, joueur2, pdv1, pdv2):
    print("*********** Level " + str(j1) + " : " + str(niveau[0]) + " --- Level " + str(j2) + " : " + str(niveau[1]) + " ***********")
    for k, value in dico.items():
        for j, val in dico[joueur1].items():
            index = val.__len__()
    classe1 = str(val[index-1])
    if classe1 == 'guerrier':
        attaque1 = random.randint(1, 3)
    elif classe1 == 'pretre':
        attaque1 = random.randint(1, 1)
    elif classe1 == 'voleur':
        attaque1 = random.randint(1, 3)
    else:
        attaque1 = random.randint(1, 1)
    for k, value in dico.items():
        for j, val in dico[joueur2].items():
            index = val.__len__()
    classe2 = str(val[index-1])
    if classe2 == 'guerrier':
        defense2 = random.randint(1,1)
    elif classe2 == 'pretre':
        defense2 = random.randint(1,2)
    elif classe2 == 'voleur':
        defense2 = random.randint(1,1)
    else:
        defense2 = random.randint(1,2)
    if (attaque1 - defense2) < 0:
        print(str(j1) + " attaque" + " (" + str(attaque1) + ") " + str(j2) + " qui se defend (" + str(defense2) + ") -->  " + str(j2) + " perd " + str(0) + " pdv ")
    else:
        print(str(j1) + " attaque" + " ("+ str(attaque1) + ") " + str(j2) + " qui se defend (" + str(defense2) + ") -->  " + str(j2) + " perd " + str((attaque1 - defense2)) + " pdv ")
    pdv[1] = pdv2 - (attaque1 - defense2)
    for k, value in dico.items():
        for j, val in dico[joueur2].items():
            index = val.__len__()
    classe2 = str(val[index-1])
    if classe2 == 'guerrier':
        attaque2 = random.randint(1,3)
    elif classe2 == 'pretre':
        attaque2 = random.randint(1,1)
    elif classe2 == 'voleur':
        attaque2 = random.randint(1,3)
    else:
        attaque2 = random.randint(1,1)
    for k, value in dico.items():
        for j, val in dico[joueur1].items():
            index = val.__len__()
    classe1 = str(val[index-1])
    if classe1 == 'guerrier':
        defense1 = random.randint(1,1)
    elif classe1 == 'pretre':
        defense1 = random.randint(1,2)
    elif classe1 == 'voleur':
        defense1 = random.randint(1,1)
    else:
        defense1 = random.randint(1,2)
    if (attaque2 - defense1) < 0:
        print(str(j2) + " attaque" + " (" + str(attaque2) + ") " + str(j1) + " qui se defend (" + str(defense1) + ") -->  " + str(j1) + " perd " + str(0) + " pdv ")
    else:
        print(str(j2) + " attaque" + " ("+ str(attaque2) + ") " + str(j1) + " qui se defend (" + str(defense1) + ") -->  " + str(j1) + " perd " + str((attaque2 - defense1)) + " pdv ")
    pdv[0] = pdv1 - (attaque2 - defense1)
    if (attaque1 - defense2) < (attaque2 - defense1):
        niveau[1] = niveau[1] + 1
        pdv[1] = (dv2 * niveau[1]) - (attaque1 - defense2)
        print("\n" + str(j2) + " gagne cette manche et passe au niveau suivant ! Calcule de son nouveau PDV...")
    if (attaque1 - defense2) > (attaque2 - defense1):
        niveau[0] = niveau[0] + 1
        pdv[0] = (dv1 * niveau[0]) - (attaque2 - defense1)
        print("\n" + str(j1) + " gagne cette manche et passe au niveau suivant ! Calcule de son nouveau PDV...")
    if pdv[0] <= 0:
        print("Partie terminée. " + str(j1) + " a perdu.")
        exit()
    if pdv[1] <= 0:
        print("Partie terminée. " + str(j2) + " a perdu.")
        exit()
    print("*********** Nouveaux PDV ***********")
    print("PDV " + str(j1) + " = " + str(pdv[0]))
    print("PDV " + str(j2) + " = " + str(pdv[1]))
    return ""


nb_persos = 0
niveaux = 10
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
joueur1 = random.randint(0,nb_persos-1)
joueur2 = random.randint(0,nb_persos-1)
while joueur1 == joueur2:
    joueur1 = random.randint(0,nb_persos-1)
    joueur2 = random.randint(0,nb_persos-1)
for k, value in dico.items():
    for j, val in dico[k].items():
        if joueur1 == k:
            j1 = j
    for h, fol in dico[k].items():
        if joueur2 == k:
            j2 = j
print("Voici les deux joueurs qui vont s'affronter : " + str(j1) + " et " + str(j2) )
tour = 1
pdv = [0] * 2
niveau_j1 = niveau[0]
niveau_j2 = niveau[1]
dv1 = lance_de_classe(joueur1)
dv2 = lance_de_classe(joueur2)
pdv[0] = dv1 * niveau_j1
pdv[1] = dv2 * niveau_j2
continuer_tour = (input("Commencer le premier tour ? (O/N) : ")).lower()
while continuer_tour != 'o' and continuer_tour != 'n':
    continuer_tour = (input("Commencer le premier tour ? (O/N) : ")).lower()
while continuer_tour == 'o':
    print(j1 + " possède : " + str(dv1) + " dv")
    print(j2 + " possède : " + str(dv2) + " dv")
    print("\n---------- TOUR " + str(tour) + " ----------")
    # print("*********** Level j1 : " + str(niveau_j1) + " --- Level j2 : " + str(niveau_j2) + " ***********")
    print("PDV " + str(j1) + " = " + str(pdv[0]))
    print("PDV " + str(j2) + " = " + str(pdv[1]))
    tour_jeu(joueur1, joueur2, pdv[0], pdv[1])
    continuer_tour = (input("Passer au tour suivant ? (O/N) : ")).lower()
    tour = tour + 1
    if continuer_tour != 'o' and continuer_tour != 'n':
        continuer_tour = (input("Passer au tour suivant ? (O/N) : ")).lower()
print("Vous avez arreter le jeu.")

