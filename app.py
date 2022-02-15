#encoding: utf-8
from Bots.BotTriste import BotTriste
from BotController import BotController
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Universitário"), BotFeliz("Feliciano")]

sys = BotController()
sys.inicio()
