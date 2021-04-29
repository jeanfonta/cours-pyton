def check_password(password):

    def length_password(password):
        if len(password) >= 10:
            return True
        else:
            return False

    def maj_password(password):
        for c in password:
            if c.isupper():
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

    def car_special(password):
        for c in password:
            if not c.isdigit() and not c.islower() and not c.isupper():
                return True
        return False


    if length_password(password) and maj_password(password) and min_password(password) and num_password(password) and car_special(password) is True:
        return True
    else:
        if length_password(password) is False:
            print("The password is not long enough")

        if maj_password(password) is False:
            print("Missing a upper case")

        if min_password(password) is False:
            print("Missing a lower case")

        if num_password(password) is False:
            print("Missing a number")

        if car_special(password) is False:
            print("Missing a special car")
        return False


def already_exist(new):
    if new in userlist:
        return False
    userlist.append(new)
    return True


def email_already_exist(mail):
    if mail in users:
        return False
    return True


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


def check_zip_code(code):
    if code >= 1000 and code <= 9999:
        return True
    return False


def check_login_lower(user):
    for c in user:
        if not c.islower:
            return False
    return True


#  The users are asked to enter their information
compteur = 1
userlist = []
users = []
answer = input("To add a new user (Y/N) : ")
while answer == "Y":
    users.append("Utilisateur n°" + str(compteur))
    compteur = compteur + 1
    name = input("Enter your name: ")
    surname = input("The surname must be different from the surname. Enter your surname: ")
    while check_nom_prenom(name, surname) is False:
        name = input("The name must be different from the surname. Enter your name: ")
        surname = input("Enter your surname: ")
    users.append(name)
    users.append(surname)

    email = input("Enter your adress mail in the following syntax: xxx@xxx.xx: ")
    while check_email(email) is False or email_already_exist(email) is False:
        email = input("Enter your adress mail in the following syntax: xxx@xxx.xx: ")
    users.append(email)

    code = int(input("Enter your zipcode: "))
    while check_zip_code(code) is False:
        code = int(input("The zipcode must be between 1000 and 9999. Enter your zipcode: "))
    users.append(code)

    username = input("Enter your login:")
    while check_login_lower(username) is False or already_exist(username) is False:
        username = input("Enter your login: ")
    users.append(username)

    password = input("Enter your password with ten caract: ")
    while check_password(password) is False:
        password = input("Incorrect password. Enter a new password : ")
    hide_password = "*" * len(password)
    users.append(hide_password)
    answer = input("To add a new user (Y/N) : ")
    if answer == "N":
        print(users)







