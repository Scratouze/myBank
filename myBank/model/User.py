import itertools
from time import sleep

from myBank.Controller.AccountController import myBank
from myBank.model.CheckingAccount import CheckingAccount
from myBank.repository.dataBase_util import addUserDB, selectAllUsers, selectByUserName, delUserDB, selectByUserId, \
    selectByUserNameAndPwd


class User(object):
    users = []
    _idCounter = itertools.count()

    def __init__(self, userName: str, pwd: str):
        self._id = next(User._idCounter)
        self._userName = userName
        self._pwd = pwd
        User.users.append(self)

    def get_id(self):
        return self._id

    def set_userName(self, userName):
        self._userName = userName

    def get_userName(self):
        return self._userName

    def set_pwd(self, pwd):
        self._pwd = pwd

    def get_pwd(self):
        return self._pwd

    @staticmethod
    def checkUsers():
        users = selectAllUsers().fetchall()
        if len(users) == 0:
            print(f"Il n'y a pas d'utilisateur créé\n{CheckingAccount.separator}")
        else:
            return users

    @staticmethod
    def createUser():
        userName = input("Entrez un nom d'utilisateur : \n")
        results = selectByUserName(userName)
        for user in results:
            if user and user[1] == userName:
                print(f"Id: {user[0]}\nNom d'utilisateur: {user[1]}\n{CheckingAccount.separator}")
                userName = input("Ce nom d'utilisateur existe déjà, veuillez entrez un autre nom d'utilisateur : \n")
        separator = "-" * 50
        while len(userName) <= 2 or len(userName) >= 19 or userName.isdigit():
            userName = input("Entrez un nom d'utilisateur entre 3 et 20 caractères contenant au moins 1 lettre : \n")
        else:
            print(f"Votre nom d'utilisateur est : {userName}")
            print(separator)
            userPwd = input("Entrez un mot de passe (minimum 8 caractères) : \n")
        while len(userPwd) == 0:
            userPwd = input("Veuillez entrer un mot de passe : \n")
        else:
            from myBank.Controller.UserController import password_check
            while not password_check(userPwd):
                userPwd = input("Veuillez entrez un mot de passe contenant au moins un chiffre, une lettre minuscule"
                                ", une lettre majuscule ainsi qu'1 caractère spécial (\'$@#%+-*!?\') : \n")

        print(f"Vos identifiants de connexion sont  : \n{userName} - {userPwd}")
        print(separator)
        addUserDB(userName, userPwd)
        return User(userName, userPwd)

    @staticmethod
    def deleteUser():
        if not User.checkUsers():
            pass
        else:
            targetUserId: int = int(input("Quel compte souhaitez vous supprimer (id) ? \n"))
            users = selectByUserId(targetUserId)
            for user in users:
                if user:
                    print(f"{CheckingAccount.separator}\nL'utilisateur {user[1]} a été supprimé\n{CheckingAccount.separator}")
                    delUserDB(targetUserId)

    @staticmethod
    def viewAllUsers():
        User.checkUsers()
        users = selectAllUsers().fetchall()
        for user in users:
            print(f"Id: {user[0]}\nNom d'utilisateur: {user[1]}\n{CheckingAccount.separator}")

    @staticmethod
    def checkUserId(Id: int):
        users = User.users
        for user in users:
            if user.get_id() == Id:
                return user

    @staticmethod
    def check(pwd: str, userName: str):
        users = User.users
        for user in users:
            if user.get_pwd() == pwd and user.get_userName() == userName:
                return user

    @staticmethod
    def connect():
        if not User.checkUsers():
            pass
        else:
            userName = input(f"Quel est votre nom d'utilisateur ?\n {CheckingAccount.separator}\n")
            userPwd = input(f"Quel est votre mot de passe ?\n {CheckingAccount.separator}\n")
            while not selectByUserNameAndPwd(userName, userPwd).fetchall():
                print(f"Identifiant ou mot de passe incorrect\n {CheckingAccount.separator}")
                userName = input(f"Quel est votre nom d'utilisateur ?\n {CheckingAccount.separator}\n")
                userPwd = input(f"Quel est votre mot de passe ?\n {CheckingAccount.separator}\n")
            sleep(0.5)
            print(CheckingAccount.separator)
            sleep(0.4)
            print(CheckingAccount.separator)
            sleep(0.3)
            print("Vous allez arriver sur la page de gestion de myBank")
            sleep(0.5)
            return myBank(userName)


def __str__(self) -> str:
    return f'id: {self.get_id()} \nlastName: {self.get_userName()} \nfirstName: {self.get_pwd()}'
