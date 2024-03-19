from kivy.config import Config
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from reminder_type import ReminderTypeApp  # Import the ReminderTypeApp

class LoginApp(App):
    def build(self):
        # Create a RelativeLayout as the root layout
        layout = RelativeLayout()
        
        # Add the background image covering the entire layout
        background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        
        # Add the login components on top of the background
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.login_button = Button(text='Login')
        self.login_button.bind(on_release=self.login)
        self.message_label = Label()
        
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_button)
        layout.add_widget(self.message_label)
        
        # Set the positions and sizes of login components using pos_hint and size_hint
        self.username_input.pos_hint = {'center_x': 0.5, 'center_y': 0.6}
        self.username_input.size_hint = (None, None)
        self.username_input.size = (400, 50)
        
        self.password_input.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.password_input.size_hint = (None, None)
        self.password_input.size = (400, 50)
        
        self.login_button.pos_hint = {'center_x': 0.5, 'center_y': 0.4}
        self.login_button.size_hint = (None, None)
        self.login_button.size = (200, 50)
        
        self.message_label.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
        
        return layout

    def login(self, instance):
        entered_username = self.username_input.text
        entered_password = self.password_input.text
        
        # Replace with your authentication logic
        if self.is_valid_credentials(entered_username, entered_password):
            self.message_label.text = 'Login successful'
            self.navigate_to_reminder_type()
        else:
            self.message_label.text = 'Invalid username or password'

    def navigate_to_reminder_type(self):
        app = ReminderTypeApp()
        app.run()

    def is_valid_credentials(self, username, password):
        # Replace with your actual validation logic
        return username == 'user123' and password == 'password123'

if __name__ == '__main__':
    LoginApp().run()
