import random

class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, msg, respostas = []):
        self.__id = id
        self.__mensagem = msg
        self.__respostas = respostas

    @property
    def id(self):
        return self.__id

    @property
    def mensagem(self):
        return self.__mensagem

    @property
    def respostas(self):
        return self.__respostas

    @respostas.setter
    def respostas(self, respostas):
        self.__respostas = respostas
    
    def getRandomResposta(self):
        return self.respostas

    def addResposta(self, resposta):
        self.respostas.append(resposta)
    
    def delResposta(self, resposta):
        self.respostas.remove(resposta)