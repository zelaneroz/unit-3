from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3
from kivymd.uix.datatables import MDDataTable
from Lessons.secure_password import encrypt_password, check_password
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
import time
from datetime import datetime

class database_handler:
    def __init__(self, namedb:str):
        self.connection = sqlite3.Connection(namedb)
        self.cursor = self.connection.cursor()
    def create_tables(self):
        query = f"""CREATE TABLE if not exists ledger(
    id INTEGER primary key,
    Date text not null,
    Category text not null,
    jpy integer not null,
    brz integer not null);"""
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
    dialog=None
    def l_popup(self,out:str):
        if not self.dialog:
            self.dialog = MDDialog(text=out, buttons=[MDFlatButton(text="Okay", on_release=self.dialog_close)], )
        self.dialog.open()
    def dialog_close(self,obj):
        self.dialog.dismiss()

    def try_login(self):
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        MainScreen.user1 = self.ids.uname.text
        query = f"SELECT * from users where uname='{uname}' or email='{uname}'"
        db = database_handler(namedb="spentio.db")
        result = db.search(query)
        if len(result)==1:
            email,uname,hashed = result[0]
            if check_password(passwd,hashed):
                self.parent.current="MainScreen"
            else:
                self.l_popup("Incorrect Password. Try again.")

        db.close()
        self.ids.uname.text = ''
        self.ids.passwd.text=''
    def register_btn(self):
        self.parent.current = "RegistrationScreen"
class RegistrationScreen(MDScreen):
    dialog = None
    def dialog_close(self,obj):
        self.dialog.dismiss()
    def login_btn(self):
        self.parent.current = "LoginScreen"
    def try_register(self):
        db = database_handler(namedb="spentio.db")
        email = self.ids.email.text
        pass1 = self.ids.pass1.text
        pass2 = self.ids.pass2.text
        uname = self.ids.uname.text
        db.run_query("SELECT * FROM users")
        email_list, uname_list = [], []

        out=""
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
            self.parent.current = "LoginScreen"
        def popup(out:str):
            if not self.dialog:
                self.dialog = MDDialog(text=out, buttons=[MDFlatButton(text="Okay", on_release=self.dialog_close)], )
            self.dialog.open()
        popup(out)


class Content(MDBoxLayout):
    def categ_pressed(self,btn_name):
        self.btn_name= btn_name
        MainScreen.category =btn_name
    def get_btn(self):
        return str(self.btn_name)
    def set_error_message(self):
        MainScreen.int_input1 = self.ids.int_input.text
    pass
class MainScreen(MDScreen):
    data_table = None
    category = None
    int_input1 = None
    user1 = None
    id_edit=None
    def on_pre_enter(self, *args):
        self.data_table = MDDataTable(
            size_hint = (.8,.45),
            pos_hint = {"center_x":.5, "center_y":.5},
            use_pagination = True,
            check = True,
            #title of the columns
            column_data = [("No.",40),
                           ("Date",50),
                           ("Category",50),
                           ("Amount (JPY)",50),
                           ("Amount (BRL)", 50)
                           ]
        )
        #self.data_table.bind(on_row_press = self.row_pressed) # method name change so its more easy to understand
        self.data_table.bind(on_check_press = self.check_pressed)
        self.add_widget(self.data_table) #add table to the GUI
        self.update(f"SELECT id,Date,Category,jpy,brz from ledger where user='{self.user1}'")
    def logout(self):
        self.parent.current='LoginScreen'
    def check_pressed(self,table,current_row):
        return current_row
    def delete(self):
        checked_rows = self.data_table.get_row_checks()
        print(checked_rows)
        db = database_handler("spentio.db")
        for r in checked_rows:
            id=r[0]
            query = f"DELETE from ledger where id={id}"
            db.run_query(query)
        db.close()
        self.update(f"SELECT id,Date,Category,jpy,brz from ledger where user='{self.user1}'")
    def add_popup(self):
        self.save_dialog = MDDialog(
            title='Add entry',
            type='custom',
            content_cls=Content(),
            buttons=[
                MDFlatButton(
                    text='CANCEL',
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text='OK',
                    on_release=self.save
                )
            ]
        )
        self.save_dialog.open()

    def close_dialog(self, obj):
        self.save_dialog.dismiss()
    def save(self,*args):
        integer = self.save_dialog.content_cls.ids.int_input.text
        date_time = datetime.fromtimestamp(time.time())
        str_date = date_time.strftime("%d %B, %Y")
        category = self.category
        print(integer,'\n\n',type(integer))
        db = database_handler("spentio.db")
        query = f"INSERT into ledger (date, category, jpy,brz,user) VALUES('{str_date}','{category}',{int(integer)},{int(integer)*.038},'{self.user1}')"
        db.run_query(query)
        db.close()

        self.save_dialog.dismiss()
        self.update(f"SELECT id,Date,Category,jpy,brz from ledger where user='{self.user1}'")
    def update(self,query):
        db=database_handler("spentio.db")
        #query = "SELECT * from ledger"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)

    def spinner_clicked(self,value):
        print(f"\nSpinner selected {value}")
        if value=='All':
            self.update(f"SELECT id,Date,Category,jpy,brz from ledger where user='{self.user1}'")
        else:
            self.update(f"SELECT id,Date,Category,jpy,brz from ledger where user='{self.user1}' and Category='{value}'")

    def edit_entry(self,*args):
        print("Edit is triggered")
        integer = self.edit_dialog.content_cls.ids.int_input.text
        category = self.category
        db = database_handler("spentio.db")
        query = f"UPDATE ledger set category='{category}',jpy={int(integer)},brz={int(integer)*.038} where id={self.id_edit} and user='{self.user1}'"
        db.run_query(query)
        db.close()
        self.edit_dialog.dismiss()
        self.update(f"SELECT id,Date,Category,jpy,brz from ledger where user='{self.user1}'")

    def close_dialog_1(self,obj):
        self.edit_dialog.dismiss()
    def edit_trig(self):
        checked_rows = self.data_table.get_row_checks()
        if len(checked_rows) ==1:
            self.id_edit = checked_rows[0][0]
            self.edit_dialog = MDDialog(
                title='Edit entry',
                type='custom',
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text='CANCEL',
                        on_release=self.close_dialog_1
                    ),
                    MDFlatButton(
                        text='OK',
                        on_release=self.edit_entry
                    )
                ]
            )
            self.edit_dialog.open()



class spentio(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
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