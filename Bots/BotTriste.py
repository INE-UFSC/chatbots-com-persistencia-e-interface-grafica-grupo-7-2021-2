from Bots.Bot import Bot
from Comando.Comando import Comando

class BotTriste(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandoBoasVindas = Comando(1, "Bom dia", self.boas_vindas())
        self.__comandoNome = Comando(2, "Qual o seu nome?", self.respostaNome())
        self.__comandoConselho = Comando(3, "Quero um conselho", self.conselho())
        self.__comandoAdeus = Comando(4, "Adeus", self.despedida())

    def apresentacao(self):
        return(f"Eu sou {self.nome}, me empresta dinheiro pra comprar café?")
 
    def mostra_comandos(self):
        return(f"""{self.__comandoBoasVindas.id} - {self.__comandoBoasVindas.mensagem}\n{self.__comandoNome.id} - {self.__comandoNome.mensagem}\n{self.__comandoConselho.id} - {self.__comandoConselho.mensagem}\n{self.__comandoAdeus.id} - {self.__comandoAdeus.mensagem}""")
    
    def executa_comando(self,cmd):

        #comandoBoasVindas = Comando(1, "Bom dia", self.boas_vindas())
        #comandoNome = Comando(2, "Qual o seu nome?", self.respostaNome())
        #comandoConselho = Comando(3, "Quero um conselho", self.conselho())
        #comandoAdeus = Comando(4, "Adeus", self.despedida())

        if cmd == 1:
            #return(self.boas_vindas())
            return self.__comandoBoasVindas.getRandomResposta()
        elif cmd == 2:
            #return(f"Eu sou {self.nome}, perguntas repetidas me deixam triste e cansado")
            return self.__comandoNome.getRandomResposta()
        elif cmd == 3:
            #return(self.conselho())
            return self.__comandoConselho.getRandomResposta()
        elif cmd == 4:
            #return(self.despedida())
            return self.__comandoAdeus.getRandomResposta()
        else:
            return ("Comando inválido")

    def boas_vindas(self):
        return("Bom dia? talvez para os outros bots...")

    def despedida(self):
        return("Mais um que se vai, eu já deveria ter percebido...")

    def conselho(self):
        return("Não confie em ninguém, principalmente em você mesmo.")
    
    def respostaNome(self):
        return(f"Eu sou {self.nome}, perguntas repetidas me deixam triste e cansado")