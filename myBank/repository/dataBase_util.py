from myBank.repository.dataBase import bdd


def createDB():
    con = bdd.cursor()
    con.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        " id INTEGER PRIMARY KEY AUTOINCREMENT,"
        " username TEXT NOT NULL,"
        " pwd TEXT NOT NULL)")
    con.close()


def addUserDB(userName: str, userPwd: str):
    values = [(userName, userPwd)]
    for value in values:
        con = bdd.cursor()
        con.execute("INSERT INTO users (username, pwd) VALUES (?, ?)", value)
        con.close()


def delUserDB(*userId: int):
    con = bdd.cursor()
    con.execute("DELETE FROM users WHERE id = ?", userId)
    con.close()


def selectAllUsers():
    con = bdd.cursor()
    users = con.execute("SELECT * FROM users")
    if users:
        return users


def selectByUserName(*userName: str):
    con = bdd.cursor()
    users = con.execute("SELECT * FROM users WHERE username = ?", userName)
    if users:
        return users


def selectByUserId(*userId: int):
    con = bdd.cursor()
    users = con.execute("SELECT * FROM users WHERE id = ?", userId)
    if users:
        return users


def selectByUserNameAndPwd(userName: str, userPwd: str):
    con = bdd.cursor()
    result = con.execute("SELECT * FROM users WHERE username= ? AND pwd = ?", (userName, userPwd))
    if result:
        return result
