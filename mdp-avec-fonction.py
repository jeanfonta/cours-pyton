def maj_(password):
    for c in password:
        if c.isupper():
            return True
    print("il manque une majuscule")


def min_(password):
    for c in password:
        if c.islower():
            return True
    print("il manque une minuscule")


def digit_(password):
    for c in password:
        if c.isdigit():
            return True
    print("il manque un chiffre")


mdp = input("entrez un mdp avec 1 min, 1 maj, 1 chiffre")
if len(mdp) >= 10:
    long_mdp = True
    if maj_(mdp) is True and min_(mdp) is True and digit_(mdp) is True and long_mdp is True:
        print("mdp ok")
else:
    print("votre mdp ne fait pas 10 c.")






