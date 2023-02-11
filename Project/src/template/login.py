import sqlite3
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class database_handler:
    def __init__(self, namedb:str):
        self.connection = sqlite3.Connection(namedb)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        query = f"""CREATE TABLE if not exists users(
    id integer primary key,
    email text not null unique,
    password text not null,
    username text not null
)"""

    def run_query(self,query:str):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def insert(self,email,password,username):
        query = f"INSERT into users VALUES('{email}','{password}','{username}')"
        self.run_query(query)

    def test_login(self, email, paswd):
        query = f"SELECT * FROM users  WHERE email = '{email}' and password='{paswd}'"
        result = self.cursor.execute(query).fetchone()
        print(result)

class LoginScreen(MDScreen):
    def try_login(self):
        email_entered = self.ids.uname.text
        pass_entered = self.ids.passwd.text
        db = database_handler(namedb="login_database.db")
        db.test_login(email=email_entered,paswd=pass_entered)

    def try_register(self):
        print("User tried to register")
        self.parent.current = "RegistrationScreen"
        #print("User tried to login")
        #print(f"Username: {self.ids.uname.text}\nPassword: {self.ids.passwd.text}")
class RegistrationScreen(MDScreen):
    def try_register(self):
        print("User tried to register")
        self.parent.current = "RegistrationScreen"

class login(MDApp):
    def build(self):
        return

db = database_handler(namedb="login_database.db")
db.create_tables()
db.close()
test = login()
test.run()
