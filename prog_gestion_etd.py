from pkg_etd.gestion_etd_list import *
from pkg_etd.gestion_etd_dico import *

etd_lst = create_etd_list()


choix = input("Que voulez vous faire? \n1) Ajouter un etudiant \n"
              "2) Supprimer un etudiant grace a nom/prenom \n3) Supprimer un etudiant grace a son matricule\n"
              "4) Modifier les infos d'un etudiant \n5) Chercher un etudiant avec son nom/prenom \n"
              "6) Ajouter/Modifier/supprimer une cote \n7) Afficher les cotes  \n8) Calculer la moyenne\n"
              "9) Donner la plus basse et la plus grande note\n")

while choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix == "5" or choix == "6" or choix == "7" or choix == "8" or choix == "9":

    if choix == "1":
        etudiant = create_etd()
        create_matricule(etd_lst, etudiant)
        add_etd_list(etd_lst, etudiant)
        continuer = input("On continue? (o/n) ").lower()
        while continuer == 'o':
            etudiant = create_etd()
            create_matricule(etd_lst, etudiant)
            add_etd_list(etd_lst, etudiant)
            continuer = input("On continue? (o/n) ").lower()
        print(etd_lst)
        "Ajout(s) pris en compte."

    if choix == "2":
        prenom = input("Quel est le prenom de l'etudiant à supprimer?\n")
        nom = input("Quel est le nom de l'etudiant à supprimer?\n")
        delete_etd_nom(nom, prenom, etd_lst)

    if choix == "3":
        matricule = input("Quel est le matricule de l'etudiant à supprimer?\n")
        delete_etd_matricule(matricule, etd_lst)

    if choix == "4":
        matricule = input("Quel est le matricule de l'etudiant à modifier?\n")
        new = create_etd()
        for etudiant in etd_lst:
            if etudiant['matricule'] == matricule:
                etudiant = new

    if choix == "5":
        nom = input("Quel est le nom de l'etudiant à rechercher?\n")
        prenom = input("Quel est le prenom de l'etudiant à rechercher?\n")
        etudiant = recherche_etd(nom, prenom, etd_lst)
        print(etudiant)

    if choix == "6":
        matricule = input("Entrez le matricule de l'etudiant\n")
        cours = input("Entrez le cours:\n")
        cote = input("Entrez la nouvelle cote:\n")
        ajout_cote = add_etd_cours_cote_list(etd_lst, matricule, cours, cote)
        print(ajout_cote)

    choix = input("Que voulez vous faire? \n1) Ajouter un etudiant \n"
                  "2) Supprimer un etudiant grace a nom/prenom \n3) Supprimer un etudiant grace a son matricule\n"
                  "4) Modifier les infos d'un etudiant \n5) Chercher un etudiant avec son nom/prenom \n"
                  "6) Ajouter/Modifier/supprimer une cote \n7) Afficher les cotes  \n8) Calculer la moyenne\n"
                  "9) Donner la plus basse et la plus grande note\n10) Stop\n")

exit("Fin du programme.")



