# from kivy.lang import Builder
# from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
#
# KV = '''
# MDFloatLayout:
#
#     MDTopAppBar:
#         title: "MDDatePicker"
#         pos_hint: {"top": 1}
#         elevation: 10
#
#     MDRaisedButton:
#         text: "Open date picker"
#         pos_hint: {'center_x': .5, 'center_y': .5}
#         on_release: app.show_date_picker()
# '''
#
#
# class Test(MDApp):
#     def build(self):
#         return Builder.load_string(KV)
#
#     def on_save(self, instance, value, date_range):
#         '''
#         Events called when the "OK" dialog box button is clicked.
#
#         :type instance: <kivymd.uix.picker.MDDatePicker object>;
#
#         :param value: selected date;
#         :type value: <class 'datetime.date'>;
#
#         :param date_range: list of 'datetime.date' objects in the selected range;
#         :type date_range: <class 'list'>;
#         '''
#         value=str(value)
#         print(instance, value, date_range)
#
#     def on_cancel(self, instance, value):
#         '''Events called when the "CANCEL" dialog box button is clicked.'''
#
#     def show_date_picker(self):
#         date_dialog = MDDatePicker()
#         date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
#         date_dialog.open()
#
#
# Test().run()
#
#
#
#
#
#
#
#
# # class Test1:
# #     def __init__(self,base):
# #         self.base=base
# #
# # class Test2(Test1):
#
# #     def __init__(self,base):
# #         super().__init__(self,base)
# #
# # t = Test1(1)
# # d = Test2(10)
# # print(d.base)
#
#
# # from kivymd.app import MDApp
# # from kivymd.uix.button import MDRectangleFlatButton
# # from kivymd.uix.dialog import MDDialog
# # from kivy.lang import Builder
# # kv = '''
# # <OtherClass>:
# #     id: other_class
# #
# # <MyApp>:
# #     MDRaisedButton:
# #         text: "Trigger OtherClass Method"
# #         on_press: app.trigger_method()
# # '''
# # Builder.load_string(kv)
# #
# # class OtherClass:
# #     def some_method(self):
# #         print("OtherClass method was called.")
# #
# # class MyApp(MDApp):
# #     def build(self):
# #         self.other_class = OtherClass()
# #         return Builder.load_string(kv)
# #
# #     def trigger_method(self):
# #         self.other_class.some_method()
# #
# # MyApp().run()
#
#
# from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# from kivy.properties import ObjectProperty
# from kivymd.uix.pickers import MDDatePicker
#
#
# class DatePickerScreen(BoxLayout)

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker

class sample(MDApp):
    def get_date(self, date):
        return date
    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()


sample().run()
