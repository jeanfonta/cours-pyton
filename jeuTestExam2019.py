''' afficher de maniere ordonee le titre des livre qui sont ecrit pars xeis et hickman et afficher leur nombre

afficher la liste des different editeur et afficher leur nombre

afficher de les titre anterieur a mon annee de naissence'''


fichier = open("livres.csv","r")
contenu = fichier.readlines()
fichier.close()

for donneTab in contenu:
    donneTab = donneTab.split('#')
    print(donneTab)
