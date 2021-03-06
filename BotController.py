from BotView import BotView
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado
import PySimpleGUI as sg
from BotDAO import BotDAO

class BotController:
    def __init__(self):
        self.__telaBots = BotView()
        self.__BotDAO = BotDAO()
        self.__bots = {'bot-feliz': BotFeliz('Feliciano'), 'bot-triste': BotTriste('Universitário'), 'bot-zangado': BotZangado('Yoda')}
        self.__bot_escolhido = self.__bots['bot-zangado']

    def inicio(self):
        self.__telaBots.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        
        while rodando:
            event, values = self.__telaBots.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Bom Dia':
                resultado = self.__bot_escolhido.executa_comando(1)

            elif event == 'Qual o seu nome?':
                resultado = self.__bot_escolhido.executa_comando(2)
            
            elif event == 'Quero um conselho':
                resultado = self.__bot_escolhido.executa_comando(3)
            
            elif event == 'Adeus':
                resultado = self.__bot_escolhido.executa_comando(4)
            
            elif event == 'Exportar':
                self.__BotDAO.add(self.__bot_escolhido)
                resultado = "Bot exportado"
            
            elif event == 'Importar':
                
                    self.__BotDAO.get(nomeBot)
                    resultado = "Bot exportado"
            
            if resultado != '':
                dados = str(resultado)
                self.__telaBots.mostra_resultado(dados)

        self.__telaBots.fim()