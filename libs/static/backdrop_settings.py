from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class OptionsMenu(MDScreen):

    header = StringProperty("Menu")

    def set_header(self, new_header):
        new_header = new_header[0].upper() + new_header[1:]
        if new_header == "Configuracoes": new_header = "Configurações"
        self.header = new_header