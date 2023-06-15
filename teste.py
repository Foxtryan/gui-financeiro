from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.app import MDApp
from kivy.lang import Builder

kvcode = """
# ScreenManager:
MDScreenManager:

    MDScreen:
        name: 'tela a'

        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: "Sou a tela A"

            MDCard:
                on_release:
                    root.current_heroes = ['hero']
                    root.current = 'tela b'
                MDHeroFrom:
                    id: 'hero_from'
                    tag: 'hero'

                    FitImage:  
                        source: "images.jpg"

    MDScreen:

        name: 'tela b'
        hero_to: hero_to

        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: "Sou a tela B"

            MDCard:
                MDHeroTo:
                    id: hero_to
                    tag: 'hero'
"""

class Aplicativo(MDApp):

    def build(self):
        return Builder.load_string(kvcode)
    
if __name__ == '__main__':
    Aplicativo().run()