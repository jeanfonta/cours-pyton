def programme():
    try:
        fichier = open("livres.csv", "r")
        contenuLivre = fichier.readlines()
        fichier.close()


        for donneTab in contenuLivre:
            donneTab = donneTab.split('#')
            print(donneTab[3],donneTab[0])


    except FileNotFoundError:
        print("mauvais nom de fichier csv ")


programme()
