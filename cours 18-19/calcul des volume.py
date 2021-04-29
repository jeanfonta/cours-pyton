def calcul_cube(nbr1):
    resultat = nbr1 * nbr1 * nbr1
    return resultat


def calcul_cylindre(nbr2, nbr3):
    import math
    resulta = math.pi * nbr2 * nbr2 * nbr3
    return resulta


def sphere(rayon):
    import math
    resultat = 4 * math.pi * rayon * rayon * rayon / 3
    return resultat


def parallepipede(longeur, largeur, hauteur):
    resultat = longeur * largeur * hauteur
    return resultat


def choisir_fonction(choix):
    if choix == 1:
        saisie1 = float(input("entree votre premier coté svp :"))

        print(calcul_cube(saisie1))

    elif choix == 2:
        saisie2 = float(input("entree le rayons svp :"))
        saisie3 = float(input("entree la hauteur svp :"))

        print(calcul_cylindre(saisie2, saisie3))

    elif choix == 3:
        print(sphere(float(input("entree votre rayon svp :"))))

    elif choix == 4:
        longeur = float(input("entree la longeur svp :"))
        largeur = float(input("entree la largeur svp :"))
        hauteur = float(input("entree la hauteur svp :"))

        print(parallepipede(longeur, largeur, hauteur))
    else:
        print("vortre choix n'est pas dans la liste ")


def menu():
    print("1=calcul du Cube\n2=calcul du Cylindre\n3=calcule de la sphere\n4=calcul du parallepipede\n")
    choisir_fonction(int(input()))


menu()
