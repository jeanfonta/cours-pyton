fichier = open("livres.csv", "r")
contenueLivre = fichier.readlines()
fichier.close()
### pouvoir extraire les auteurs ou meme grace a un auteur retrouver tout ce qu'il a pu faire et meme les année de parution

tableauTitreAuteur = []

def titreAuteur():
    for donneeTab in contenueLivre:
        donneeTab = donneeTab.split('#')
        if donneeTab[2] == "Margaret Weis & Tracy Hickman":
            tableauTitreAuteur.append([donneeTab[1], donneeTab[2]])


titreAuteur()


