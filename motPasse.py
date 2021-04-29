### fonction qui verifie si il y a bien 10 caractere minimum


def verifieNombreCaractere(mdp):
    return len(mdp) >= 10


"""fonction qui verifie si il y a bien une majuscule dans le mdp"""


def majuscule(mdp):
    for caractere in mdp:
        if caractere.isupper():
            print("il y as bien une majuscule")
            break
        else:
            print("il faut une majuscule dans le mot de passe")


"""fonction qui regarde si il y a bien une minuscule dans le mdp"""


def minuscule(mdp):
    for caractere in mdp:
        if caractere.islower():
            print("il y as bien une minuscule")
            break
        else:
            print("il faut une minuscule au mot de passe svp :")


"""fonction qui regarde si il y a bien un chiffre dans le mdp"""


def chiffre(mdp):
    for caratere in mdp:
        if caratere.isdigit():
            print("il y as bien un chiffre")
            break
        else:
            print("il manque un chiffre dans le mot de passe")


"""fonction qui regarde si il y a bien un caractere special dans le mdp"""


def special(mdp):
    for caractere in mdp:
        if not caractere.isdigit() and not caractere.islower() and not caractere.isupper():
            print("il y a bien un caractere special")
            break
        else:
            print("il manque un caractere special")


"""fonction qui demande a l'utilisateur d'entree un mdp et qui sert a lancer toute les fonctions de mon code """


def programme():
    mdp = input("entree votre mot de passe svp : ")
    verifieNombreCaractere(mdp)
    majuscule(mdp)
    minuscule(mdp)
    chiffre(mdp)
    special(mdp)


programme()
