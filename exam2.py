def codePaire(code):
    return code % 2 == 0


def programme():
    try:
        fichier = open("cities.csv", "r")
        contenu = fichier.readlines()
        fichier.close()
        tabCode = []
        for donneeFichier in contenu:
            donneeFichier = donneeFichier.rstrip("\n").replace("\"", "")
            donneeSpliter = donneeFichier.split(',')
            if donneeSpliter[1].isdigit():
                codePostal = int(donneeSpliter[1])
                if codePostal >= 5000 and codePostal <= 5100:
                    if codePaire(codePostal):
                        tabCode.append(donneeSpliter)

    except FileNotFoundError:
        print("mauvais fichier csv")

    return tabCode

programme()

for i in programme():
    print(i[1], i[2])
