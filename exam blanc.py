from random import randint

#  tableau de 100 entier de nombre aléatoir de 0 a 20 comprit

tableau = []
for i in range(100):
    tableau.append(randint(0, 20))

#  demande saisie et le convertit en entier

entree_utilisateur = int(input('Entrer la valeur à recherché : '))

#  condition sur la saisie utilisateur

if entree_utilisateur < 0:
    print("L'élément recherché n'existe pas dans le tableau")

print(tableau[entree_utilisateur])
print(tableau)
