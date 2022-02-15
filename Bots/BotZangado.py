from Bots.Bot import Bot
from Comando.Comando import Comando

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = self.cria_comandos([1, 'Bom dia', 'Olá, como você vai me encher o saco hoje?',
                                              2, 'Qual o seu nome?', self.nome,
                                              3, 'Quero um conselho', 'Não tenho filho desse tamanho.',
                                              4, 'Adeus', 'Já vai tarde. Adeus.'])

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

    def apresentacao(self):
        return(f"Grrrrrr. Meu nome é {self.nome} e eu te odeio!")
 
    def mostra_comandos(self):
        return(f"""{self.__comandoBoasVindas.id} - {self.__comandoBoasVindas.mensagem}\n{self.__comandoNome.id} - {self.__comandoNome.mensagem}\n{self.__comandoConselho.id} - {self.__comandoConselho.mensagem}\n{self.__comandoAdeus.id} - {self.__comandoAdeus.mensagem}""")
    
    def executa_comando(self,cmd):
        try:
            cmd = int(cmd)
        except:
            resposta = 'NÃO ENTENDI!!!'
        else:
            if cmd not in self.comandos.keys():
                resposta = 'FALA PORTUGUÊS!!!'
            else:
                resposta = self.comandos[cmd].getRandomResposta()

        return resposta

    def boas_vindas(self):
        return("Olá, como você vai me encher o saco hoje?")
    
    def conselho(self):
        return("Não tenho filho desse tamanho.")

    def despedida(self):
        return("Já vai tarde. Adeus.")
    
    def respostaNome(self):
        return(f"{self.nome}, quantas vezes tenho que repetir?")