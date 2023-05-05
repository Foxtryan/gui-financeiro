from kivy.properties import ListProperty
from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors, palette

from kivymd.theming import ThemableBehavior
from kivy.uix.widget import Widget
from kivymd.uix.list import (
    ILeftBody,
    OneLineAvatarListItem,
)

class ShowerColorOneLine(OneLineAvatarListItem):
    color = ListProperty()

class LeftWidget(ILeftBody, Widget):
    pass

class BaseDialog(ThemableBehavior, ModalView):
    pass

class DialogChangeTheme(BaseDialog):

    def __init__(self, *args, **kwargs):
        super(DialogChangeTheme, self).__init__(*args, **kwargs)


    def set_list_colors_themes(self):
        for name_theme in palette:
            self.ids.rv.data.append(
                {
                    "viewclass": "ShowerColorOneLine",
                    "color": get_color_from_hex(colors[name_theme]["500"]),
                    "text": name_theme,
                }
            )