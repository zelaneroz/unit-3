from kivymd.app import MDApp
import warnings
warnings.simplefilter('ignore')

class currencyconverter(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
        self.currency="EUR"
    def build(self):
        return

    def set_amount(self):
        number = self.root.ids.user_num.text

    def to_usd(self):
        if self.currency=="JPY":
            self.count *= 0.0077
        if self.currency=="EUR":
            self.count *= 0.0071
        self.currency=="USD"
test = currencyconverter()
test.run()