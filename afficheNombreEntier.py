def afficheNombre(nbr1,nbr2):
    if nbr1 > nbr2:
        print("le plus grand est", nbr1, "le plus petit est ", nbr2)
    elif nbr1 < nbr2:
        print("le plus grand est", nbr2, "le plus petit est le", nbr1)
    else:
        print("il sont egal")


def programme():
    nbr1 = int(input("entree votre premier nombre svp :"))
    nbr2 = int(input("entree votre deuxieme nombre svp :"))
    afficheNombre(nbr2,nbr1)


programme()