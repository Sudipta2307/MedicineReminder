from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv = """
WindowManager:
    FirstWindow:
    SecondWindow:

<FirstWindow>:
    name: "first"

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        Label:
            text: "First Screen"
            font_size: 32

        Button:
            text: "Next Screen"
            font_size: 32
            on_release: app.root.current = "second"

<SecondWindow>:
    name: "second"

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        Label:
            text: "Second Screen"
            font_size: 32

        Button:
            text: "Go Back"
            font_size: 32
            on_release: app.root.current = "first"
"""
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class AwesomeApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    AwesomeApp().run()
