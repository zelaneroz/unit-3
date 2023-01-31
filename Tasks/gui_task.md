**Table of Contents**
1. [Example 1](#ex1)
2. [Example 2](#ex2)
3. [Example 3](#ex3)
4. [Task 1](#task_1)
5. [Task 2](#task_2)

# Example 1 <a name="ex1"></a>
**Python**
```.py
from kivymd.app import MDApp

class example1(MDApp):
    def build(self):
        return

test = example1()
test.run()
```
**Kivy**
```.kv
Screen:
    size: 500,500

    MDLabel:
        text:"Hello World"
        halign: "center"
        font_size: "34pt"
```
**Output**
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_e2989g/Screen Shot 2023-01-31 at 11.43.08 AM.png)


# Example 2 <a name="ex2"></a>
**Python**
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

**Kivy**
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

**Output**
![](../../../../../var/folders/y0/hqzvd0zj4gd8wqkm8l5zck3c0000gn/T/TemporaryItems/NSIRD_screencaptureui_sIZeNo/Screen Shot 2023-01-31 at 11.48.29 AM.png)

# Example 3 <a name="ex3"></a>

# Task 1 <a name="task_1"></a>

# Task 2 <a name="task_2"></a>