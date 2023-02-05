from kivymd.app import MDApp
import warnings
warnings.simplefilter('ignore')

class q40(MDApp):
    def build(self):
        return
    def change_color(self):
        if self.root.ids.main1.md_bg_color == "#FFFFFF":
            self.root.ids.main1.md_bg_color = "#000000"
            self.root.ids.btn1.md_bg_color = "#FF0000"
            #self.root.ids.txt.text_color = "#FFFFFF"
        else:
            self.root.ids.main1.md_bg_color = "#FFFFFF"
            self.root.ids.btn1.md_bg_color = "#0000FF"
            #self.root.ids.txt.text_color = "#000000"

test = q40()
test.run()