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
        
        # Background image covering the entire layout
        background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        
        # Create username and password input fields
        self.username_input = self.create_text_input('Username', 0.6)
        self.password_input = self.create_text_input('Password', 0.5, password=True)
        
        # Create login button
        self.login_button = Button(text='Login', size_hint=(None, None), size=(200, 50))
        self.login_button.pos_hint = {'center_x': 0.5, 'center_y': 0.4}
        self.login_button.bind(on_release=self.login)
        
        # Message label to display login status
        self.message_label = Label(pos_hint={'center_x': 0.5, 'center_y': 0.3})
        
        # Add widgets to layout
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_button)
        layout.add_widget(self.message_label)
        
        return layout

    def create_text_input(self, hint_text, center_y, password=False):
        """Helper method to create a TextInput widget."""
        text_input = TextInput(
            hint_text=hint_text, 
            multiline=False, 
            password=password, 
            size_hint=(None, None), 
            size=(400, 50),
            pos_hint={'center_x': 0.5, 'center_y': center_y}
        )
        return text_input

    def login(self, instance):
        """Handle login button click."""
        entered_username = self.username_input.text.strip()
        entered_password = self.password_input.text.strip()
        
        if self.is_valid_credentials(entered_username, entered_password):
            self.message_label.text = 'Login successful'
            self.navigate_to_reminder_type()
        else:
            self.message_label.text = 'Invalid username or password'

    def navigate_to_reminder_type(self):
        """Navigate to the ReminderTypeApp."""
        app = ReminderTypeApp()
        app.run()

    def is_valid_credentials(self, username, password):
        """Validate user credentials. Replace with actual logic."""
        return username == 'user123' and password == 'password123'

if __name__ == '__main__':
    LoginApp().run()
