from Bots.Bot import Bot
from Comando.Comando import Comando

class BotTriste(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = self.cria_comandos([1, 'Bom dia', 'Bom dia? talvez para os outros bots...',
                                              2, 'Qual o seu nome?', self.nome,
                                              3, 'Quero um conselho', 'Não confie em ninguém, principalmente em você mesmo.',
                                              4, 'Adeus', 'Mais um que se vai, eu já deveria ter percebido...'])
        
        #self.__comandoBoasVindas = Comando(1, "Bom dia", self.boas_vindas())
        #self.__comandoNome = Comando(2, "Qual o seu nome?", self.respostaNome())
        #self.__comandoConselho = Comando(3, "Quero um conselho", self.conselho())
        #self.__comandoAdeus = Comando(4, "Adeus", self.despedida())

    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos

    def cria_comandos(self, comandos):
        mapeamento = {}
        for i in range (0, len(comandos), 3):
            c = Comando(comandos[i], comandos[i + 1], comandos[i + 2])
            mapeamento[comandos[i]] = c

        return mapeamento

    def executa_comando(self, cmd):
        try:
            cmd = int(cmd)
        except:
            resposta = 'Não entendi nada.'
        else:
            if cmd not in self.comandos.keys():
                resposta = 'Boa tentativa.'
            else:
                resposta = self.comandos[cmd].getRandomResposta()

        return resposta

    def apresentacao(self):
        return(f"Eu sou {self.nome}, me empresta dinheiro pra comprar café?")
 
    def mostra_comandos(self):
        return(f"""{self.__comandoBoasVindas.id} - {self.__comandoBoasVindas.mensagem}\n{self.__comandoNome.id} - {self.__comandoNome.mensagem}\n{self.__comandoConselho.id} - {self.__comandoConselho.mensagem}\n{self.__comandoAdeus.id} - {self.__comandoAdeus.mensagem}""")
    
    def executa_comando(self,cmd):

        #comandoBoasVindas = Comando(1, "Bom dia", self.boas_vindas())
        #comandoNome = Comando(2, "Qual o seu nome?", self.respostaNome())
        #comandoConselho = Comando(3, "Quero um conselho", self.conselho())
        #comandoAdeus = Comando(4, "Adeus", self.despedida())

        try:
            cmd = int(cmd)
        except:
            resposta = 'Não entendi, amigo!'
        else:
            if cmd not in self.comandos.keys():
                resposta = 'Boa tentativa, mas não entendi o que você quer :D'
            else:
                resposta = self.comandos[cmd].getRandomResposta()

        return resposta

    def boas_vindas(self):
        return("Olá, como você está? Eu estou triste.")

    def despedida(self):
        return("Tchau...")