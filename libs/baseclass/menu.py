from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, NumericProperty
from libs.baseclass.configuracoes import Configuracoes 

## spend color #b95820
## earned color #2e935f

class Menu(Screen):
    
    # Center Top
    lbl_fluxo_titulo = StringProperty("Fluxo de Caixa")
    lbl_fluxo_total = StringProperty("36.000")
    progress_entradas = NumericProperty(60)
    progress_saidas = NumericProperty(40)

    pass