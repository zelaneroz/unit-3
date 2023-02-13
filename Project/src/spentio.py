from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3

class database_handler:
    def __init__(self, namedb:str):
        self.connection = sqlite3.Connection(namedb)
        self.cursor = self.connection.cursor()
    def create_tables(self):
        query = f"""CREATE TABLE if not exists users(
        email text not null unique,
        password text not null,
        username text not null unique
    )"""
    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()
    def close(self):
        self.connection.close()
    def insert(self, email, password, username):
        query = f"INSERT into users VALUES('{email}','{password}','{username}')"
        self.run_query(query)
    def test_login(self, email, passwd):
        self.cursor.execute("SELECT * FROM users")
        email_list, uname_list = [], []
        for i in self.cursor.fetchall():
            email_list.append(i[0])
            uname_list.append(i[1])
        output = ""
        if (email in email_list or email in uname_list) and email != "":
            self.cursor.execute(f"SELECT password FROM users where email='{email}' or uname='{email}'")
            for j in self.cursor:
                if passwd == j[0]:
                    output = "You have successfully logged in!"
                else:
                    output = "Incorrect Password"
        else:
            output = "Incorrect Email"
        print(output)
        if output == "You have successfully logged in!":
            return True

    def test_register(self,email,pass1,pass2,uname):
        out = ""
        self.cursor.execute("SELECT * FROM users")
        email_list, uname_list = [], []
        for i in self.cursor.fetchall():
            email_list.append(i[0])
            uname_list.append(i[1])
        print(email_list)
        print(uname_list)
        print(type(email), type(pass1),type(pass2),type(uname))
        if email in email_list or uname in uname_list:
            out="User already exists"
        if pass1!=pass2:
            out="Password does not match. Try again"
        if email=="" or pass1=="" or pass2=="" or uname=="":
            out="Please enter values."
        else:
            out="User successfully added."
        print(out)
        if out == "User successfully added.":
            print(out)
            self.cursor.execute(f"INSERT into users values ('{email}', '{uname}','{pass1}')")
            self.connection.commit()
            return True
        #Must test if pass1 is same as pass2
        #Must test if no field is empty
        #Must test if uname is already existing
        #Test if email is already existing
class LoginScreen(MDScreen):
    def try_login(self):
        email_entered = self.ids.uname.text
        pass_entered = self.ids.passwd.text
        db = database_handler(namedb="spentio.db")
        if db.test_login(email=email_entered, passwd=pass_entered) == True:
            self.parent.current = "MainScreen"
    def register_btn(self):
        self.parent.current = "RegistrationScreen"
class RegistrationScreen(MDScreen):
    def login_btn(self):
        print("User tried to register")
        self.parent.current = "MainScreen"
    def try_register(self):
        db = database_handler(namedb="spentio.db")
        email = self.ids.email.text
        pass1 = self.ids.pass1.text
        pass2 = self.ids.pass2.text
        uname = self.ids.uname.text
        if db.test_register(email=email, pass1=pass1, pass2=pass2, uname=uname) == True:
            self.parent.current = "LoginScreen"
class MainScreen(MDScreen):
    pass
class spentio(MDApp):
    def build(self):
        return

db = database_handler(namedb="spentio.db")
db.create_tables()
db.close()
test = spentio()
test.run()

#COLOR SCHEMES
#Light - FFF0EB
#Mid - FDB9D2
#Dark - F08DA9