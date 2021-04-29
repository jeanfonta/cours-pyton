def minuscul(maill):
    for caractere in maill:
        if caractere.islower():
            break
        else:
            print("il y a bien une minuscule")


def majuscul(maill):
    for caractere in maill:
        if caractere.isupper():
            break
        else:
            print("il y a bien une majuscule")


def programme():
    maill = input("entree votre maill svp")
    majuscul(maill)
    minuscul(maill)

programme()