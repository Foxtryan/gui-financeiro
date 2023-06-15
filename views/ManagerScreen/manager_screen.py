import os

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, NoTransition

from kivy.utils import get_color_from_hex

from kivymd.app import MDApp

from views.screens import screens


class ManagerScreen(ScreenManager):
    dialog_wait = None
    _screen_names = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.transition = NoTransition()

    def on_current(self, *args):
        super().on_current(*args)


    def create_screen(self, name_screen):
        if name_screen not in self._screen_names:
            self._screen_names.append(name_screen)
            exec(f"import views.{screens[name_screen]}")
            self.app.load_all_kv_files(
                os.path.join(self.app.directory, "views", screens[name_screen].split(".")[0])
            )
            view = eval(
                f'views.{screens[name_screen]}.{screens[name_screen].split(".")[0]}()'
            )
            view.name = name_screen
            return view


    def switch_screen(self, screen_name: str) -> None:
        def switch_screen(*args):
            if screen_name not in self._screen_names:
                self.open_dialog()
                screen = self.create_screen(screen_name)
                self.add_screen(screen)

            self.current = screen_name
            self.dialog_wait.dismiss()

        if screen_name not in self._screen_names:
            self.open_dialog()
            Clock.schedule_once(switch_screen)
        else:
            self.current = screen_name

    def open_dialog(self) -> None:
        if not self.dialog_wait:
            image = Image(
                source="assets/images/loading.gif",
                size_hint=(0.15, 0.15),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            self.dialog_wait = ModalView(
                background="assets/images/modal-bg.png",
            )
            self.dialog_wait.add_widget(image)
        self.dialog_wait.open()

    def add_screen(self, view) -> None:
        self.add_widget(view)