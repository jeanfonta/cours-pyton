fichier = open("fichier.txt","w")
fichier.write("voila le fichier")
fichier.close()

tab=["avions\n","moto\n","voiture\n","jenny\n","jean\n","karda"]
fichier = open("fichier.txt", "w")
fichier.writelines(tab)
fichier.close()

fichier = open("fichier.txt", "a")
fichier.write("ben saute renaud avec le slip open bar")
fichier.close()



fichier = open("fichier.txt", "r")
contenuFichier = fichier.readlines()
print(contenuFichier)
fichier.close()
