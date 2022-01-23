from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class WidgetsExample(GridLayout):
    my_text = StringProperty("0")
    clicks = 0
    count_enabled = BooleanProperty(False)
    # slider_value_txt = StringProperty('50')
    def on_button_clicked(self):
        if self.count_enabled:
            self.clicks += 1
            print("Button clicked")
            self.my_text = f"{self.clicks}"
        else:
            print('button click when switch is off')

    def on_toggle_button_state(self, widget):
        print(f'toggle state: {widget.state}')
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print(f'Switch {widget.active}')

    # def on_slider_value(self, widget):
    #     self.slider_value_txt = str(int(widget.value))
    #     print(f'Slider value: {widget.value}')

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-bt"
        size = dp(100)
        widgets = []
        for num in range(1, 101):
            b = Button(text=str(num), size_hint=(None,None), size=(size,size))
            self.add_widget(b)
            widgets.append(b)

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text='A')
        b2 = Button(text='B')
        self.add_widget(b1)
        self.add_widget(b2)"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


TheLabApp().run()