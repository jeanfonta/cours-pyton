# PROGRAM CHECK PASSWORD
mdp = input("veuillez encoder un mdp avec min. 10 c., 1 maj., 1 min. et 1 chiffre:" "\n")
withOutSpace = mdp.replace(" ", "")   # TO REMOVE WHITESPACE
mdp_ok = False   # VARIABLE'S DECLARATION TO ENTER IN THE LOOP

while mdp_ok is not True:
    if len(withOutSpace) >= 10:
        upper_ok = False
        lower_ok = False
        digit_ok = False
        for c in withOutSpace:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                upper_ok = True
            if c in "abcdefghijklmnopqrstuvwxyz":
                lower_ok = True
            if c in "1234567890":
                digit_ok = True
        if upper_ok and lower_ok and digit_ok is True:
                mdp_ok = True
                print("mdp ok")
        else:
            if upper_ok is not True:
                print("il manque une majuscule""\n")
            if lower_ok is not True:
                print("il manque une minuscule""\n")
            if digit_ok is not True:
                print("il manque un chiffre""\n")
            mdp = input("veuillez encoder un mdp avec min. 10 c., 1 maj., 1 min. et 1 chiffre: ""\n")
            withOutSpace = mdp.replace(" ", "")
    else:
        print("votre mdp ne fait pas 10 caractéres""\n")
        mdp = input("veuillez encoder un mdp avec min. 10 c., 1 maj., 1 min. et 1 chiffre: " "\n")
        withOutSpace = mdp.replace(" ", "")

