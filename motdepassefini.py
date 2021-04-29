def check_password(mdp):
    def car_spe(password):
        for c in password:
            if not c.isupper() and not c.islower() and not c.isdigit():
                return True
        return False

    def maj_(password):
        for c in password:
            if c.isupper():
                return True
        return False

    def min_(password):
        for c in password:
            if c.islower():
                return True
        return False

    def digit_(password):
        for c in password:
            if c.isdigit():
                return True
        return False

    # mdp = input("entrez un mdp avec 1 min, 1 maj, 1 chiffre")
    if len(mdp) >= 10:
        long_mdp = True
        if maj_(mdp) is True and min_(mdp) is True and digit_(mdp) is True and long_mdp is True and car_spe(mdp) is True:
            print("mdp ok")
        else:
            if not maj_(mdp):
                print('pas maj')
            if not min_(mdp):
                print('pas min')
            if not digit_(mdp):
                print('pas chiffre')
            if not car_spe(mdp):
                print("pas carac spécial")
    else:
        print("votre mdp ne fait pas 10 c.")


# email check


def check_email(balec):

    email_split = email.split('@')

    if len(email_split) != 2:
        exit("Your email address is invalid.")

    for caractere in email_split[0]:
        if not (ord(caractere) in list(range(97, 123))) and caractere not in ('.', '-'):
            exit("Invalid syntax")

    email_domaine_split = email_split[1].split('.')
    if len(email_domaine_split) != 2:
        exit("Second part not xxx.xxx syntax.")

    for caractere in email_split[1]:
        if not (ord(caractere) in list(range(97, 123))) and caractere != '.':
            exit("Invalid char in second part.")

    if len(email_domaine_split[1]) not in (2, 3):
        exit("Invalid suffix.")



def check_nom_prenom(name, surname):
    if name != surname:
        return True
    return False


def check_zip_code(code):
    if code >= 1000 and code <= 9999:
        return True
    return False


def check_login_lower(user):
    for c in user:
        if not c.islower:
            return False
    return True


surname = input("Enter your surname: ")
name = input("The surname must be different from the name. Enter your name:")

while check_nom_prenom(name, surname)is False:
    surname = input("The surname and the name cannot be the same. Enter your surname again: ")
    name = input("The surname and the name cannot be the same. Enter your name again:")

