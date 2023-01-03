import sys
from time import sleep

from myBank.model.CheckingAccount import CheckingAccount
from myBank.repository.dataBase import bdd
from myBank.model.User import User


def password_check(pwd) -> bool:
    SpecialChar = ['$', '@', '#', '%', '+', '-', '*', '!', '?']
    result = True
    if not any(char.isdigit() for char in pwd):
        result = False
    if not any(char.isupper() for char in pwd):
        result = False
    if not any(char.islower() for char in pwd):
        result = False
    if not any(char in SpecialChar for char in pwd):
        result = False
    if result:
        return result


def Connection():
    sleep(0.1)
    print(
        f"{CheckingAccount.separator}\n{CheckingAccount.separator}\nBienvenue sur myBank\n{CheckingAccount.separator}"
        f"\n{CheckingAccount.separator}")
    sleep(0.5)
    menu = "Choisissez parmi les options suivantes \n" \
           "1: Connection \n" \
           "2: Afficher tout les utilisateurs \n" \
           "3: Création utilisateur \n" \
           "4: Supprimer un utilisateur \n" \
           "5: Quitter \n" \
           "Votre choix -> "

    menu_choice = ["1", "2", "3", "4", "5"]
    while True:
        user_choice = ""
        while user_choice not in menu_choice:
            user_choice = input(menu)
            if user_choice not in menu_choice:
                print("\n Veuillez choisir une option valide")
                print(CheckingAccount.separator)
            else:
                print(CheckingAccount.separator)
                match user_choice:
                    case "1":
                        User.connect()
                    case "2":
                        User.viewAllUsers()
                    case "3":
                        User.createUser()
                    case "4":
                        User.deleteUser()
                    case "5":
                        print(f"A bientôt !\n{CheckingAccount.separator}")
                        bdd.commit()
                        sys.exit()
