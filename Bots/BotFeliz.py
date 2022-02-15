from Bots.Bot import Bot
from Comando.Comando import Comando

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = self.cria_comandos([1, 'Bom dia', 'Olá, como você está? Obrigado por me chamar!',
                                              2, 'Qual o seu nome?', self.nome,
                                              3, 'Quero um conselho', 'Sorria, a vida é uma só!',
                                              4, 'Adeus', 'Tenha um bom dia!'])

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
        return(f"Meu nome é {self.nome}! Fico muito feliz de conversar com você :) !!!")
 
    def mostra_comandos(self):
        amostra = ''
        for comando in self.comandos.values():
            amostra += f'{comando.id} - {comando.mensagem}\n'
        
        return amostra
    
    def executa_comando(self, cmd):
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
        return("Olá, como você está? Obrigado por me chamar!")

    def despedida(self):
        return("Tenha um bom dia!")