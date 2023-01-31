from kivymd.app import MDApp
import warnings
warnings.simplefilter('ignore')
class example1(MDApp):
    def build(self):
        self.screen.ids.text_field_error.bind(on_text_validate=self.set_error_message,on_focus=self.set_error_message)
        return self
    def set_error_message(self,instance_textfield):
        self.screen.ids.text_field_error.error=True
    def close(self):
        exit()
test=example1()
test.run()