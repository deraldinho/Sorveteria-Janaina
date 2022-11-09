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
        :return: nao a retorno
        '''
        self.tamanho=self.verif_Tamanho(tamanho)
        self.codigo=self.verif_Codigo(codigo)
        self.calc_preco()
        self.calc_precoTotal()

    def calc_preco(self):
        '''
        :param self retorna o valor constante pregado no começo do codigo
        :return: retorna as constantes dependendo do pedido;
        '''
        aux = self.codigo+'_'+self.tamanho
        if(aux == 'TR_P'):
            return TR_P
        elif(aux == 'TR_M'):
            return TR_M
        elif(aux == 'TR_G'):
            return TR_G
        elif (aux == 'ES_P'):
            return ES_P
        elif (aux == 'ES_M'):
            return ES_M
        elif (aux == 'ES_G'):
            return ES_G
        elif (aux == 'PR_P'):
            return PR_P
        elif (aux == 'PR_M'):
            return PR_M
        elif (aux == 'PR_G'):
            return PR_G

    def calc_precoTotal(self):
        aux = self.codigo + '_' + self.tamanho
        if(aux == 'TR_P'):
            self.precoTotal+= TR_P
        elif(aux == 'TR_M'):
            self.precoTotal += TR_M
        elif(aux == 'TR_G'):
            self.precoTotal += TR_G
        elif (aux == 'ES_P'):
            self.precoTotal += ES_P
        elif (aux == 'ES_M'):
            self.precoTotal += ES_M
        elif (aux == 'ES_G'):
            self.precoTotal += ES_G
        elif (aux == 'PR_P'):
            self.precoTotal += PR_P
        elif (aux == 'PR_M'):
            self.precoTotal += PR_M
        elif (aux == 'PR_G'):
            self.precoTotal += PR_G

    def verif_Tamanho(self, tamanho):
        if(tamanho == 'P' or tamanho == 'p'):
            return 'P'
        elif (tamanho == 'M' or tamanho == 'm'):
            return 'M'
        elif (tamanho == 'G' or tamanho == 'g'):
            return 'P'
        else:
            print('Tamanho ou Codigo INVALIDO!!!')
    def verif_Codigo(self,codigo):
        if(codigo == 'TR' or codigo == 'tr'):
            return 'TR'
        elif (codigo == 'ES' or codigo == 'es'):
            return 'ES'
        elif (codigo == 'PR' or codigo == 'pr'):
            return 'PR'
        else:
            print('Tamanho ou Codigo INVALIDO!!!')

    def verif_sabor(self):
        if(self.codigo == 'TR' or self.codigo == 'tr'):
            return 'Tradicionais'
        elif (self.codigo == 'ES' or self.codigo == 'es'):
            return 'Especiais'
        elif (self.codigo == 'PR' or self.codigo == 'pr'):
            return 'Premium'
        else:
            pass

class Interface:

    '''
        Class destinada a interface, ela ira apresentar as escolha e coletar os inputs.
    '''
    control = 'S'
    count = 0
    pedido = Pedidos()
    def loop(self):
        self.home()
        while(True):
            if self.control == 'S' or self.control == 's':
                self.pedido.add_pedido(input('Entre com Tamanho do Pote desejado (P/M/G): '),input('Entre com codigo do sabor desejado (TR/ES/PR): '))
                print(f'Você Pediu um sorvete sabor {self.pedido.verif_sabor()} de R$ {self.pedido.calc_preco()}')
                print('------------------------------------------------------------------------------------------')
                self.control = input('Deseja Pedir mais alguma coisa? (S/N)')

            elif self.control == 'N' or self.control == 'n':
                print(f'O total a se pago é: R$ {self.pedido.precoTotal}');
                break
            else:
                pass
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
