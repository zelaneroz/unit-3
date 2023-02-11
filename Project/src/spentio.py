from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager

class LoginScreen(MDScreen):
    def try_login(self):
        print("User tried to login")
        print(f"Username: {self.ids.uname.text}\nPassword: {self.ids.passwd.text}")
    def register_btn(self):
        print("User tried to register")
        self.parent.current = "RegistrationScreen"
class RegistrationScreen(MDScreen):
    def try_register(self):
        print("User tried to register")
        self.parent.current = "SignupScreen"
    def login_btn(self):
        print("User tried to register")
        self.parent.current = "MainScreen"
class MainScreen(MDScreen):
    pass
class spentio(MDApp):
    def build(self):
        return

test = spentio()
test.run()

#COLOR SCHEMES
#Light - FFF0EB
#Mid - FDB9D2
#Dark - F08DA9