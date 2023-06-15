from kivy.uix.screenmanager import Screen
from views.ManagerScreen.manager_screen import ManagerScreen

from kivy.uix.button import Button
from views.HomeScreen.home import HomeScreen
from views.TesteScreen.teste import TesteScreen

class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
