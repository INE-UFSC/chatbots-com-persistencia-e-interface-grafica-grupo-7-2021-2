import PySimpleGUI as sg 

# View do padrão MVC
class BotView():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window("Fale com o Bot", self.__container ,font=("Helvetica", 14))

    def tela_consulta(self):
        self.__container = [
            [sg.Text('Selecione a ação desejada:')],
            [sg.Button('Bom Dia'), sg.Button('Qual seu nome?'), sg.Button('Quero um Conselho'), sg.Button('Adeus')],
            [sg.Text('', key='resultado')]
        ]
        self.__window = sg.Window("Fale com o Bot", self.__container ,font=("Helvetica", 14))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()