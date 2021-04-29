'''moi = "je t'aime mon amour"

ma = moi.split(' ')

print(ma[1])'''


def programme():
    try:
        fichier = open("cities.csv", "r")
        contenu = fichier.readlines()
        fichier.close()
        tabDonne = []

        for donneeTableau in contenu:
            donneeSpliter = donneeTableau.split(',')
            ville = donneeSpliter[2]
            if ville[1] == "C":
                tabDonne.append(donneeSpliter)
                print(donneeSpliter[1], ville)
    except FileNotFoundError:
        print("mauvaise entree de fichier")


programme()
