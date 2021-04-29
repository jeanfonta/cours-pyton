def check_password(mdp):

    def lengt_password(password):
        if len(password) >= 10:
            return True
        return False

    def maj_password(password):
        for c in password:
            if c in "AZERTYUIOPMLKJHGFDSQWXCVBN":
                return True
            return False

    def min_password(password):
        for c in password:
            if c.islower():
                return True
            return False

    def num_password(password):
        for c in password:
            if c.isdigit():
                return True
            return False

    if lengt_password(mdp) and maj_password(mdp) and min_password(mdp) and num_password(mdp) is True:
        return True
    else:
        if lengt_password(mdp) is False:
            print("longeur")

        if maj_password(mdp) is False:
            print("majuscule")

        if min_password(mdp) is False:
            print("minuscule")

        if num_password(mdp) is False:
            print("chiffre")
        return False
# email check



def check_email(email):

    email_split = email.split('@')

    if len(email_split) != 2:
        return False


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


def check_zip_code (code):
    if code >= 1000 and code <= 9999:
        return True
    return False


def check_login_lower(user):
    for c in user:
        if not c.islower:
            return False
    return True

#  The users are asked to enter their information




utilisateurs = []


for i in range(1, 2):
    """name = input("Enter your name: ")
    surname = input("The surname must be different from the surname. Enter your surname: ")
    while check_nom_prenom(name, surname) is False:
        name = input("The name must be different from the surname. Enter your name: ")
        surname = input("Enter your surname: ")

    utilisateurs.append(name)
    utilisateurs.append(surname)

    email = input("Enter your adress mail in the following syntax: xxx@xxx.xx: ")
    while check_email(email) is False:
        email = input("Enter your adress mail in the following syntax: xxx@xxx.xx: ")
    utilisateurs.append(email)

    code = int(input("Enter your zipcode: "))
    while check_zip_code(code) is False:
        code = int(input("The zipcode must be between 1000 and 9999. Enter your zipcode: "))
    utilisateurs.append(code)

    username = input("Enter your login: ")
    while check_login_lower(username) is False:
        username = input("Enter your login: ")
    utilisateurs.append(username)"""

    password = input("Enter your password with ten caract: ")
    while check_password(password) is False:
        password = input("Enter your password with ten caracters: ")
    utilisateurs.append(password)







print(utilisateurs)





