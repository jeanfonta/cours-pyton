def majuscule(mdp):
    for caractere in mdp:
        if caractere.isupper():
            return True
    return False


def minuscule(mdp):
    for caractere in mdp:
        if caractere.islower():
            return True
    return False


def chiffre(mdp):
    for caractere in mdp:
        if caractere.isdigit():
            return True
    return False


def special(mdp):
    for caractere in mdp:
        if not caractere.isupper() and not caractere.islower() and not caractere.isdigit():
            return True
    return False


def afficherMotDePasse(mdp):
    compteur = 0
    while compteur < len(mdp):
        compteur = compteur + 1
        print("*", end="")


def longueur(mdp):
    if len(mdp) >= 10:
        return True
    return False


def motDePasseOk(mdp):
    if minuscule(mdp) and majuscule(mdp) and chiffre(mdp) and special(mdp) and longueur(mdp):
        return True
    return False


def verifieNomEtPrenom(nom, prenom):


def programme():
    utilisateur = []
    mdp = ""
    while not motDePasseOk(mdp):
        mdp = input(
            "entree un mot de passe qui comprend 1 chiffre + 1 majuscule + 1 minuscule + 1 caractere spécial et doit contenir 10 caractere minimum")

    utilisateur.append(mdp)

    afficherMotDePasse(utilisateur[0])


programme()
