def choixTva():
    tva = int(input("votre choix tva\n1=0%\n2=6%\n3=12\n4=18%\n5=21%"))
    if tva == 1:
        print("vous avez choisi de ne pas avoir de tva ")
    elif tva == 2:
        print("vous avez choisi de d'avoir 6% de tva")
    elif tva == 3:
        print("vous avez choisis une tva a 12%")
    elif tva == 4:
        print("vous avez choisis d'avoir une tva a 18%")
    elif tva == 5:
        print("vous avez choisi d'avoir une tva a 21%")
    return tva


def nombreDarticle():
    article = int(input("entree le nombre d'article svp"))
    return article


def prixUnitaire():
    prix = float(input("entree le prix hors tva svp"))
    return prix


print(choixTva() * nombreDarticle() * prixUnitaire())
