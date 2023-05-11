from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, NumericProperty
from libs.baseclass.configuracoes import Configuracoes 
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
## spend color #b95820
## earned color #2e935f
from libs.static.customprogressbar import CustomProgressBar


class Menu(Screen):
    
    # Center TOP
    progress_entradas = NumericProperty(60)
    progress_saidas = NumericProperty(40)

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

        # Left Top
        # Atuais
        self.caixa_residual = 14100.22
        self.entrada = 24520.96
        self.saida = 19230.32
        # Total
        self.total_caixa = 14100.22
        self.total_entrada = 44261.12
        self.total_saida = 32230.45
        
        self.lt_total = self.total_entrada - self.total_saida # Valor a ser somado a caixa residual do prox. mes
        self.fluxo_caixa = self.caixa_residual + self.entrada - self.saida


    # main_screen Constroi ao acessar a tela Main_SCreen - Menu.
    def construir_cards(self):
        self.desenhar_lt_card()
        self.ids['lbl_fluxo_caixa'].text = "{:.3f}".format(self.fluxo_caixa / 1000)

        
    def desenhar_lt_card(self):

        self.ids['graph_gasto_mensal'].clear_widgets()

        App_accent_color = MDApp.get_running_app().theme_cls.accent_color
        App_text_color = MDApp.get_running_app().text_color
        App_light_text_color = MDApp.get_running_app().light_text_color
        
        graph_colors = ['#1E90FF', '#2e935f', '#b95820']

        # ProgressBar triplo
        progress = CustomProgressBar(size=(145,145), pos=(5, 25))
        progress.background_color = App_accent_color
        progress.max_value = [self.total_caixa, self.total_entrada, self.total_saida]
        progress.value = [self.caixa_residual, self.entrada, self.saida]
        progress.primary_color = graph_colors[0]
        progress.secondary_color = graph_colors[1]
        progress.tertiary_color = graph_colors[2]
 
        column_x = 166
        v_caixa = "{:.3f} / {:.3f}".format(self.caixa_residual/1000, self.total_caixa/1000)
        v_entrada = "{:.3f} / {:.3f}".format(self.entrada/1000, self.total_entrada/1000)
        v_saida = "{:.3f} / {:.3f}".format(self.saida/1000, self.total_saida/1000)
        normalized_lt_total = "R$: {:.3f}".format(self.lt_total/1000)

        glayout = MDRelativeLayout()
        glayout.add_widget(progress)
        glayout.add_widget(MDLabel(text="Fluxo Mensal", adaptive_width=True, bold=True, theme_text_color='Custom', text_color=App_text_color, pos=(100,92)))
        glayout.add_widget(MDLabel(text="CAIXA RESIDUAL", font_style='Overline', theme_text_color='Custom', text_color=App_light_text_color, pos=(column_x,55)))
        glayout.add_widget(MDLabel(text=v_caixa, font_style='Body2', bold=True, theme_text_color='Custom', text_color=graph_colors[0], pos=(column_x,35)))
        glayout.add_widget(MDLabel(text="ENTRADA", font_style='Overline', theme_text_color='Custom', text_color=App_light_text_color, pos=(column_x,10)))
        glayout.add_widget(MDLabel(text=v_entrada, font_style='Body2', bold=True, theme_text_color='Custom', text_color=graph_colors[1], pos=(column_x,-10)))
        glayout.add_widget(MDLabel(text="SAÍDA", font_style='Overline', theme_text_color='Custom', text_color=App_light_text_color, pos=(column_x,-35)))
        glayout.add_widget(MDLabel(text=v_saida, font_style='Body2', bold=True, theme_text_color='Custom', text_color=graph_colors[2], pos=(column_x,-55)))
        glayout.add_widget(MDLabel(text="Fim do Mês:", font_style='Overline', theme_text_color='Custom', text_color=App_light_text_color, pos=(40,5)))
        glayout.add_widget(MDLabel(text=normalized_lt_total, font_style='Body1', bold=True, theme_text_color='Custom', text_color=App_text_color, pos=(40,-10)))

        self.ids['graph_gasto_mensal'].add_widget(glayout)

