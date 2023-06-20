from kivymd.app import MDApp
from views.ManagerScreen.manager_screen import ManagerScreen

class Financeiro(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_screen = ManagerScreen()

        self.colors = {
            "text": "#f7f8f8",
            "text_off": "#a1a1a5",
            "background": "#3A3480",
            "dark": "#2f2a68",
            "selected": "#683FFC",

            "medio": "#5432CC",
            "distorc": "#A48BFD"
        }

    def build(self):
        
        self.manager_screen.add_widget(self.manager_screen.create_screen("menu"))
        return self.manager_screen


if __name__ == '__main__':
    Financeiro().run()