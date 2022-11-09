TR_P = 6.00
TR_M = 10.00
TR_G = 18.00
ES_P = 7.00
ES_M = 12.00
ES_G = 21.00
PR_P = 8.00
PR_M = 14.00
PR_G = 24.00

class Pedidos:
    '''
    Essa classe serve para armazenar os dados e tratalos de forma correta
    '''
    def __init__(self):
        '''
            a 'Pedidos.__init__()' ser como estanciamentos para variaveis
        '''
        self.codigo = ''
        self.tamanho = ''
        self.preco = 0.00
        self.precoTotal = 0.00

    def add_pedido(self, tamanho, codigo):
        '''
        :param tamanho: tamanho do sorvete
        :param codigo: codigo do sorte
        :return: True ou False parametro booleano
        '''
        if not self.verif_Tamanho(tamanho):
            return False
        elif(not self.verif_Codigo(codigo)):
            return False
        else:
            self.tamanho = tamanho
            self.codigo = codigo
            self.calc_preco()
            self.calc_precoTotal()
            return True

    def calc_preco(self):
        aux = self.codigo+'_'+self.tamanho
        if(aux == 'TR_P' or aux == 'tr_p'):
            return TR_P
        elif(aux == 'TR_M' or aux == 'tr_m'):
            return TR_M
        elif(aux == 'TR_G' or aux == 'tr_g'):
            return TR_G
        elif (aux == 'ES_P' or aux == 'es_p'):
            return ES_P
        elif (aux == 'ES_M' or aux == 'es_m'):
            return ES_M
        elif (aux == 'ES_G' or aux == 'es_g'):
            return ES_G
        elif (aux == 'PR_P' or aux == 'pr_p'):
            return PR_P
        elif (aux == 'PR_M' or aux == 'pr_m'):
            return PR_M
        elif (aux == 'PR_G' or aux == 'pr_g'):
            return PR_G
        else:
            return False
    def calc_precoTotal(self):
        aux = self.codigo + '_' + self.tamanho
        if(aux == 'TR_P' or aux == 'tr_p'):
            self.precoTotal+= TR_P
        elif (aux == 'TR_M' or aux == 'tr_m'):
            self.precoTotal += TR_M
        elif (aux == 'TR_G' or aux == 'tr_g'):
            self.precoTotal += TR_G
        elif (aux == 'ES_P' or aux == 'es_p'):
            self.precoTotal += ES_P
        elif (aux == 'ES_M' or aux == 'es_m'):
            self.precoTotal += ES_M
        elif (aux == 'ES_G' or aux == 'es_g'):
            self.precoTotal += ES_G
        elif (aux == 'PR_P' or aux == 'pr_p'):
            self.precoTotal += PR_P
        elif (aux == 'PR_M' or aux == 'pr_m'):
            self.precoTotal += PR_M
        elif (aux == 'PR_G' or aux == 'pr_g'):
            self.precoTotal += PR_G
        else:
            return False

    def verif_Tamanho(self, tamanho):
        if(tamanho == 'P' or tamanho == 'p'):
            return 'P'
        elif (tamanho == 'M' or tamanho == 'm'):
            return 'M'
        elif (tamanho == 'G' or tamanho == 'g'):
            return 'P'
        else:
            return False
    def verif_Codigo(self,codigo):
        if(codigo == 'TR' or codigo == 'tr'):
            return 'TR'
        elif (codigo == 'ES' or codigo == 'es'):
            return 'ES'
        elif (codigo == 'PR' or codigo == 'pr'):
            return 'PR'
        else:
            return False

    def verif_sabor(self):
        if(self.codigo == 'TR' or self.codigo == 'tr'):
            return 'Tradicionais'
        elif (self.codigo == 'ES' or self.codigo == 'es'):
            return 'Especiais'
        elif (self.codigo == 'PR' or self.codigo == 'pr'):
            return 'Premium'
        else:
            return False

class Interface:

    control = 'S'
    count = 0
    pedido = Pedidos()
    def loop(self):
        self.home()
        while(True):
            if self.control == 'S' or self.control == 's':
                if not self.pedido.add_pedido(input('Entre com Tamanho do Pote desejado (P/M/G): '),input('Entre com codigo do sabor desejado (TR/ES/PR): ')):
                    print('Tamanho ou Codigo INVALIDO!!!')
                else:
                    print(f'Você Pediu um sorvete sabor {self.pedido.verif_sabor()} de R$ {self.pedido.calc_preco()}')
                print('------------------------------------------------------------------------------------------')
            elif self.control == 'N' or self.control == 'n':
                print(f'O total a se pago é: R$ {self.pedido.precoTotal}');
                break
            self.control = input('Deseja Pedir mais alguma coisa? (S/N)')
    def home(self):
        print('Bem vindo a Soveteria  Janaina Lessa de Paula')
        print(
            '|----------------------------------------------------Cardapio----------------------------------------------------|')
        print(
            '|    Código  |   Descrição               |   Tamanho P(500ml)   |    Tamanho M(1000ml)   |   Tamanho G(2000ml)   |')
        print(
            '|    TR      |   Sabores Tradicionais    |   R$  6,00           |    R$  10,00           |   R$  18,00           |')
        print(
            '|    ES      |   Sabores Especiais       |   R$  7,00           |    R$  12,00           |   R$  21,00           |')
        print(
            '|    PR      |   Sabores Premium         |   R$  8,00           |    R$  14,00           |   R$  24,00           |')
        print(
            '|----------------------------------------------------------------------------------------------------------------|')

if __name__ == '__main__':
    screen = Interface()
    screen.loop()
