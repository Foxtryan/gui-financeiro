from kivy.config import Config
Config.set('graphics', 'resizable', False)

# kivymd
from kivymd.app import MDApp

# kivy
from kivy.lang import Builder
from kivy.utils import get_color_from_hex as C
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# others
import os
import libs.baseclass
from libs.static.dialog_change_theme import DialogChangeTheme

_WIDTH = 900
_HEIGHT = 615
_TITLE = "Foxtryan"
_VERSION = "Alpha 0.1"

class Interface(ScreenManager):

    def __init__(self, *args, **kwargs):
        super(Interface, self).__init__(*args, **kwargs)

    def set_screen(self, new_screen):
        self.current = new_screen

#     def back_screen(self):
#         actual = self.current
#         screen_list = {
#             'main_screen': 'menu',
#             'configuracoes': 'menu',
#         }
#         if actual not in screen_list.keys():
#             self.set_screen('menu')
#         else:
#             self.set_screen(screen_list[actual])

class FoxApp(MDApp):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.title = _TITLE
        self.version = _VERSION
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_hue = '900'
        self.theme_cls.accent_palette = "Indigo"
        self.text_color = "#f7f8f8"
        self.light_text_color = "#E6E6FA"  #"#8c92d4"
        self.custom_background_color = "#1b2168" #"#434880"
        #self.theme_cls.theme_style = "Dark"


    def build(self):
        
        Window.size = (_WIDTH, _HEIGHT)
        # static - screens load
        location = os.path.dirname(os.path.abspath(__file__))
        load_path = os.path.join(location, "libs", "static", "kv")
        for file in os.listdir(load_path):
            Builder.load_string(open(load_path+"\\"+file, encoding="utf-8").read())
            
        # interface - screens load
        location = os.path.dirname(os.path.abspath(__file__))
        load_path = os.path.join(location, "libs", "kv")
        for file in os.listdir(load_path):
            if file != "interface.kv": 
                Builder.load_string(open(load_path+"\\"+file, encoding="utf-8").read())
        main_widget = Builder.load_string(open("libs/kv/interface.kv", encoding="utf-8").read())
        return main_widget

    # static - themes
    def switch_theme_style(self):

        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def show_dialog_change_theme(self):

        self.dialog_change_theme = DialogChangeTheme()
        self.dialog_change_theme.set_list_colors_themes()
        self.dialog_change_theme.open()

if __name__ == '__main__':
    FoxApp().run()