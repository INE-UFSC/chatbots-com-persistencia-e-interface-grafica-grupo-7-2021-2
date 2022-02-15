from DAO import DAO
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado
from Bots.Bot import Bot

class BotDAO(DAO):
    def __init__(self):
        super().__init__('bots.pkl')
    
    def add(self, bot: Bot):
        if isinstance(bot, Bot):
            super().add(bot.nome, bot.comandos)
    
    def get(self, nome: str):
        if isinstance(nome, str):
            super().get(nome)
    
    def remove(self, nome: str):
        if isinstance(nome, str):
            return super().remove(nome)