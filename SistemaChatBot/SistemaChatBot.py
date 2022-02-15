from Bots.Bot import Bot
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        self.__bot = None
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)
    
    def boas_vindas(self):
        print('Olá, este é o sistema de de chatbots da empresa {self.__empresa}')
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print("Os chat bots disponíveis no momento são:")
        for index, bot in enumerate(self.__lista_bots):
            print(f'{index + 1} - Bot: {bot.nome} - Mensagem de apresentação: {bot.apresentacao()}')
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        while True:
            num_bot = input('Digite o número do chat bot desejado:')
            if not num_bot.isnumeric():
                print("Erro. Escolha um número")
            elif int(num_bot) > len(self.__lista_bots) or int(num_bot) < 1:
                print(f"Escolha um bot entre 1 e {len(self.__lista_bots)}")
            else:
                break
        
        num_bot = int(num_bot)
        self.__bot = self.__lista_bots[num_bot - 1]
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        comando = input('Digite o comando desejado (ou -1 para fechar o comando):')
        try:
            comando = int(comando)
            if comando == -1:
                return True
            else: 
                print(self.__bot.executa_comando(comando))
        except:
            print(self.__bot.executa_comando(comando))
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while True:
            self.mostra_comandos_bot()
            if self.le_envia_comando(): break
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
