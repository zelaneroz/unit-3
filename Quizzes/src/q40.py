from kivymd.app import MDApp
import warnings
warnings.simplefilter('ignore')

class q40demo(MDApp):
    def __init__(self, **kwargs):
        self.bind(active=self.set_chip_bg_co)
    def build(self):
        return

    def close(self):
        exit()

    def change_bg_color(self):

        #white- FFFFFF
        #black -000000



test = q40demo()
test.run()