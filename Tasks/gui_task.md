# Example 1 <a name="ex1"></a>
### **Python**
```.py
from kivymd.app import MDApp

class example1(MDApp):
    def build(self):
        return

test = example1()
test.run()
```
### **Kivy**
```.kv
Screen:
    size: 500,500

    MDLabel:
        text:"Hello World"
        halign: "center"
        font_size: "34pt"
```
### **Output**
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_e2989g/Screen Shot 2023-01-31 at 11.43.08 AM.png)


# Example 2 <a name="ex2"></a>
### **Python**
```pycon
from kivymd.app import MDApp

class ex2(MDApp):
    def build(self):
        return
    def close(self):
        exit()

test = ex2()
test.run()
```

### **Kivy**
```.kv
Screen:
    size: 500,500

    MDBoxLayout:
        pos_hint: {"center_x":.5}
        size_hint: .7,.7
        md_bg_color: "#fdfcdc"
        orientation: "vertical"

        MDLabel:
            text:"Hello World"
            halign: "center"
            font_size: "34pt"

        MDRaisedButton:
            text: "Close"
            size_hint: .5,1
            font_size: "34pt"
            pos_hint: {"center_x":.5}
            md_bg_color: "#407167"
            on_press:
                app.close()
```

### **Output**
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_sIZeNo/Screen Shot 2023-01-31 at 11.48.29 AM.png)

# Example 3 <a name="ex3"></a>
### **Python**
```pycon
from kivymd.app import MDApp

class ex3(MDApp):
    def build(self):
        return

    def change_author(self,name):
        self.root.ids.text.text = f"Author {name}"

test = ex3()
test.run()
```

### **Kivy**
```.kv
Screen:
    size: 500,500

    MDLabel:
        id: text
        text: "Slay"
        font_style: "H1"
        pos_hint: {"center_x":.5, "center_y":.8}
        halign: "center"
        valign: "top"
        text_color: "#000000"
    MDBoxLayout:
        pos_hint: {"center_x":.5,"center_y":.5}
        size_hint: .7,.2
        orientation: "horizontal"

        MDChip:
            text: "Author A"
            pos_hint: {"center_y":.5}
            icon_right: "close-circle-outline"
            md_bg_color: "#003049"
            text_color: "#FFFFFF"
            on_press: app.change_author("A")
        MDChip:
            text: "Author B"
            pos_hint: {"center_y":.5}
            icon_right: "close-circle-outline"
            md_bg_color: "#D62828"
            text_color: "#FFFFFF"
            on_press: app.change_author("B")
        MDChip:
            text: "Author C"
            pos_hint: {"center_y":.5}
            icon_right: "close-circle-outline"
            md_bg_color: "#F77F00"
            on_press: app.change_author("C")
        MDChip:
            text: "Author D"
            pos_hint: {"center_y":.5}
            icon_right: "close-circle-outline"
            md_bg_color: "#FCBF49"
            text_color: "#FFFFFF"
            on_press: app.change_author("D")
        MDChip:
            text: "Author E"
            pos_hint: {"center_y":.5}
            icon_right: "close-circle-outline"
            md_bg_color: "#EAE2B7"
            text_color: "#FFFFFF"
            on_press: app.change_author("E")
```

### **Output**
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_4zl6s3/Screen Shot 2023-01-31 at 12.52.17 PM.png)

![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_3AhB2D/Screen Shot 2023-01-31 at 12.52.37 PM.png)


# Task 1 <a name="task_1"></a>
### **Python**
```pycon
from kivymd.app import MDApp
class task1(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.converted=0
        self.amount=0
        self.type="eur"
    def build(self):
        return
    def set_input(self):
        input = self.root.ids.user_input.text
        if input.isnumeric()==False:
            self.root.ids.output.text = "Please enter an integer"
        else:
            self.amount = int(input)
    def to_jpy(self):
        converted=0
        converted = round(self.amount*141.16)
        self.root.ids.output.text = f"¥ {converted}"
        
    def to_usd(self):
        converted=0
        converted = round(self.amount*1.08)
        self.root.ids.output.text = f"$ {converted}"

test=task1()
test.run()
```

### **Kivy**
```.kv
Screen:
    size: 500,500

    MDBoxLayout:
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint: .6,.6
        orientation: "vertical"
        MDLabel:
            text: "Currency Converter"
            font_size: "60"
            halign: "center"
            bold: True
        MDTextField:
            id: user_input
            hint_text: "Enter amount in EUR"
            font_size: 40
            on_text:
                app.set_input()
        MDBoxLayout:
            pos_hint:{"center_x":.5}
            orientation: "horizontal"
            MDLabel:
                text:"Click to Convert"
                font_size: "30px"
                text_color: "grey"
            MDRaisedButton:
                md_bg_color: "red"
                text: "JPY"
                on_release:
                    app.to_jpy()
            MDRaisedButton:
                text: "USD"
                md_bg_color: "blue"
                on_release:
                    app.to_usd()
        MDLabel:
            id: output 
            text: ""
            halign:"center"
            bold:True
```

### **Output**
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_0ZbXFI/Screen Shot 2023-01-31 at 4.04.57 PM.png)
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_EcwSjC/Screen Shot 2023-01-31 at 4.09.34 PM.png)
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_GOtX3X/Screen Shot 2023-01-31 at 4.09.12 PM.png)
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_CNXyxC/Screen Shot 2023-01-31 at 4.07.59 PM.png)

### UML Diagram

### Flowchart

### Wireframe



# Task 2 <a name="task_2"></a>