from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class homePage(Screen):
    def __init__(self, **kwargs):
        super(homePage, self).__init__(**kwargs)
        self.layout = GridLayout()
        self.layout.rows = 5
        self.layout.padding = (50, 0, 50, 0)
        self.layout.spacing = [20, 10]

        # Action Row
        self.action_row = ActionRow()
        self.layout.add_widget(self.action_row)

        # Add the above layout to this screen
        self.add_widget(self.layout)

class ActionRow(BoxLayout):
    def __init__(self, **kwargs):
        super(ActionRow, self).__init__(**kwargs)
        self.padding = (0, 0, 0, 10)
        button_font_size = 15
        button_width = 80
        button_height = 20
        self.statScreen = Button(font_size=button_font_size, text="Stats/Wounds", size_hint=(.4, .2))
        self.add_widget(self.statScreen)
        self.attackScreen = Button(font_size=button_font_size, text="Attacks/Skills", size_hint=(.4, .2))
        self.add_widget(self.attackScreen)
        self.lootScreen = Button(font_size=button_font_size, text="Loot", size_hint=(.4, .2))
        self.add_widget(self.lootScreen)
        self.commonRollScreen = Button(font_size=button_font_size, text="Common Roll DCs", size_hint=(.4, .2))
        self.add_widget(self.commonRollScreen)
        self.characterDetailScreen = Button(font_size=button_font_size, text="Character Details", size_hint=(.4, .2))
        self.add_widget(self.characterDetailScreen)


class ParahumanApp(App):
    def build(self):
        screen_manager = ScreenManager(transition=FadeTransition())
        screen_manager.add_widget(homePage(name='home_page'))
        return screen_manager


if __name__ == '__main__':
    ParahumanApp().run()
