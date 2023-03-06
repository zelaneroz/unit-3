# from kivymd.app import MDApp
# from kivymd.uix.menu import MDDropdownMenu,MDDropdownItem
# from kivymd.uix.floatlayout import MDFloatLayout
# from kivy.lang import Builder
#
# KV = '''
# MDFloatLayout:
#     MDDropDownItem:
#         id: dropdown_item
#         text: 'A'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#         on_release: dropdown.open()
#
#     MDDropDownMenu:
#         id: dropdown
#         items: [{'text': 'A'}, {'text': 'B'}, {'text': 'C'}]
#         width_mult: 4
# '''
#
# class DropdownButton(MDApp):
#     def build(self):
#         return Builder.load_string(KV)
#
# DropdownButton().run()
integer = 'abc'
print(integer.isdigit())