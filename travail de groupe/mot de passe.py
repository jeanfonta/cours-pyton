motDePasse = input("entree votre mot de passe qui doit contenir 10 lettre, 1 majuscule, 1 minuscule et 1 chiffre :")
nbrCar = motDePasse.__len__()
while nbrCar < 10:
    motDePasse = input("entree votre mot de passe ")

listChiffre = \
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
listMinuscule = \
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
     "y", "z"]
listMajuscule = \
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
     "Y", "Z"]
