from kivymd import mdapp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.picker import DatePicker, TimePicker


kv = """
WindowManager:
    FirstWindow:
    SecondWindow:
    ThirdWindow:

<FirstWindow>:
    name: "first"

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'background.jpg'  # Add the background image here

    RelativeLayout:
        Image:
            source: 'medilogo.png'  # Add the path to your logo
            size_hint: None, None
            size: 100, 100
            pos_hint: {'center_x': 0.5, 'top': 0.9}

        Label:
            text: "Login Page"
            font_size: 32
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'center_x': 0.5, 'top': 0.75}

        TextInput:
            hint_text: "Username"
            multiline: False
            size_hint: None, None
            size: 300, 50
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}

        TextInput:
            hint_text: "Password"
            multiline: False
            password: True
            size_hint: None, None
            size: 300, 50
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Button:
            text: "Login"
            font_size: 32
            size_hint: None, None
            size: 150, 50
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            background_color: 0, 0.50196078431, 0.60196078431, 2

            on_release: app.root.current = "second"

<SecondWindow>:
    name: "second"
    
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'background.jpg'  # Add the background image here


    RelativeLayout:
        
        Label:
            text: "CHOOSE YOUR REMINDER"
            font_size: 28
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'center_x': 0.5, 'top': 0.75}

        Button:
            id: healthCheckButton
            text: "HEALTH CHECK UP"
            size_hint: None, None
            size: 200, 70
            pos_hint: {'center_x': 0.5, 'top': 0.6}
            background_color: 0, 0.50196078431, 0.60196078431, 2
            on_release: app.root.current = "third"

        Button:
            id: medicineButton
            text: "MEDICINE"
            size_hint: None, None
            size: 200, 70
            pos_hint: {'center_x': 0.5, 'top': 0.45}
            background_color: 0, 0.50196078431, 0.60196078431, 2
            on_release: app.root.current = "first"

        Button:
            id: labTestButton
            text: "LAB TEST"
            size_hint: None, None
            size: 200, 70
            pos_hint: {'center_x': 0.5, 'top': 0.3}
            background_color: 0, 0.50196078431, 0.60196078431, 2
            on_release: app.root.current = "first"
            
<ThirdWindow>:
    name: "third"

    RelativeLayout:
        Image:
            source: 'background.jpg'  # Add the background image here
            size: root.size

        Label:
            text: "Check Up"
            font_size: 24
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'center_x': 0.5, 'top': 0.9}

        TextInput:
            id: venueEditText
            hint_text: "Venue"
            multiline: False
            size_hint: None, None
            size: 326, 50
            pos_hint: {'center_x': 0.5, 'top': 0.75}

        TextInput:
            id: doctorsNameEditText
            hint_text: "Doctor's Name"
            multiline: False
            size_hint: None, None
            size: 326, 50
            pos_hint: {'center_x': 0.5, 'top': 0.65}

        Label:
            text: "CHOOSE DATE AND TIME"
            font_size: 19
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'center_x': 0.5, 'top': 0.55}

        BoxLayout:
            orientation: "horizontal"
            size_hint: None, None
            size: 326, 50
            pos_hint: {'center_x': 0.5, 'top': 0.48}
            
            DatePicker:
                id: healthCheckDatePicker
                size_hint: None, None
                size: 163, 50
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            TimePicker:
                id: healthCheckTimePicker
                size_hint: None, None
                size: 163, 50
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Button:
            id: confirmHealthCheckButton
            text: "Confirm Checkup"
            font_size: 16
            size_hint: None, None
            size: 200, 50
            pos_hint: {'center_x': 0.5, 'top': 0.25}
            background_color: 0, 0.39215686274, 0.59607843137, 1  # Color: #006498

            on_release: app.root.current = "first"

"""
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    def show_date_picker(self):
        content = MyDatePicker()
        self.popup = Popup(title='Pick a Date', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
        content.bind(on_date=self.on_date_select)
        self.popup.open()

    def show_time_picker(self):
        content = MyTimePicker()
        self.popup = Popup(title='Pick a Time', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
        content.bind(on_time=self.on_time_select)
        self.popup.open()

    def on_date_select(self, instance, value):
        self.ids.healthCheckDatePicker.text = value.strftime('%Y-%m-%d')
        self.popup.dismiss()

    def on_time_select(self, instance, value):
        self.ids.healthCheckTimePicker.text = value.strftime('%H:%M:%S')
        self.popup.dismiss()

class MyDatePicker(DatePicker):
    def __init__(self, **kwargs):
        super(MyDatePicker, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (300, 300)

class MyTimePicker(TimePicker):
    def __init__(self, **kwargs):
        super(MyTimePicker, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (300, 300)


class AwesomeApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    AwesomeApp().run()
