from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3
from kivymd.uix.datatables import MDDataTable
from Lessons.secure_password import encrypt_password, check_password
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout

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
    def search(self,query:str):
        result = self.cursor.execute(query).fetchall()
        return result
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
        print(type(email), type(pass1),type(pass2),type(uname))
        if email in email_list or uname in uname_list:
            out="User already exists"
        if email=="" or pass1=="" or pass2=="" or uname=="":
            out="Please enter values."
class LoginScreen(MDScreen):
    def try_login(self):
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        query = f"SELECT * from users where uname='{uname}' or email='{uname}'"
        db = database_handler(namedb="spentio.db")
        result = db.search(query)
        print(result)
        if len(result)==1:
            email,uname,hashed = result[0]
            if check_password(passwd,hashed):
                print("Login successful")
                self.parent.current = "MainScreen"
        if db.test_login(email=uname, passwd=passwd) == True or db.test_login(email,passwd)==True:
            self.parent.current = "MainScreen"
        db.close()
    def register_btn(self):
        self.parent.current = "RegistrationScreen"
class RegistrationScreen(MDScreen):
    dialog = None
    def dialog_close(self,obj):
        self.dialog.dismiss()
    def login_btn(self):
        print("User tried to register")
        self.parent.current = "MainScreen"
    def try_register(self):
        db = database_handler(namedb="spentio.db")
        email = self.ids.email.text
        pass1 = self.ids.pass1.text
        pass2 = self.ids.pass2.text
        uname = self.ids.uname.text
        db.run_query("SELECT * FROM users")
        email_list, uname_list = [], []
        def popup(out:str):
            if not self.dialog:
                self.dialog=MDDialog(text=out, buttons=[MDFlatButton(text="Okay", on_release=self.dialog_close)],)
            self.dialog.open()
        out=""
        print("Data: ", email,pass1,pass2,uname,"\n")
        for i in db.cursor.fetchall():
            email_list.append(i[0])
            uname_list.append(i[1])
        if email in email_list or uname in uname_list:
            out += "User already exists.\n"
        elif email == "" or pass1 == "" or pass2 == "" or uname == "":
            out += "Please enter required fields.\n"
        elif pass1!=pass2:
            out+="Password does not match. Try again.\n"
            self.ids.pass1.error=True
            self.ids.pass2.error = True
        else:
            hash = encrypt_password(pass1)
            query = f"INSERT into users values ('{email}', '{uname}','{hash}')"
            db.run_query(query)
            db.close()
            print("Registration completed.")
            self.parent.current = "LoginScreen"
        popup(out)

class Content(MDBoxLayout):
    pass
class MainScreen(MDScreen):
    data_table = None
    def on_pre_enter(self, *args):
        #b4 the screen is created the code is run
        self.data_table = MDDataTable(
            size_hint = (.8,.45),
            pos_hint = {"center_x":.5, "center_y":.5},
            use_pagination = False,
            check = True,
            #title of the columns
            column_data = [("No.",40),
                           ("Date",50),
                           ("Category",50),
                           ("Amount",50)
                           ]
        )
        #self.data_table.bind(on_row_press = self.row_pressed) # method name change so its more easy to understand
        self.data_table.bind(on_check_press = self.check_pressed)
        self.add_widget(self.data_table) #add table to the GUI
        self.update()
    def check_pressed(self,table,current_row):
        print("A check mark was pressed", current_row)
    def delete(self):
        checked_rows = self.data_table.get_row_checks()
        print(checked_rows)
        db = database_handler("spentio.db")
        for r in checked_rows:
            id=r[0]
            query = f"DELETE from ledger where Number={id}"
            db.run_query(query)
        db.close()
        self.update()

    def save(self):
        self.save_dialog = MDDialog(
            title='Enter an Integer',
            type='custom',
            content_cls=Content(),
            buttons=[
                MDFlatButton(
                    text='CANCEL',
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text='OK',
                    on_release=self.get_integer
                )
            ]
        )
        self.save_dialog.open()

    def close_dialog(self, obj):
        self.save_dialog.dismiss()
    def get_integer(self,*args):
        integer = self.save_dialog.content_cls.ids.int_input.text
        if integer.isdigit():
            print(f"The amount entered is {integer}")
        else:
            print("Please enter a valid integer")
        self.save_dialog.dismiss()

    def update(self):
        db=database_handler("spentio.db")
        query = "SELECT * from ledger"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)

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