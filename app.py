#encoding: utf-8
from Bots.BotTriste import BotTriste
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Universitário"), BotFeliz("Feliciano")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
