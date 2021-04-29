def jeux():
    import random
    nombre_choisi = random.randint(0, 100)

    saisie_utilisateur = -1
    while saisie_utilisateur != nombre_choisi:
        saisie_utilisateur = int(input("entree votre nombre entre 0 et 100 svp :"))
        print(saisie_utilisateur)
        if nombre_choisi < saisie_utilisateur:
            print("votre nombre est plus grand")
        elif nombre_choisi > saisie_utilisateur:
            print("votre nombre est petit")
        else:
            print("bravo vous evez trouver")


jeux()
