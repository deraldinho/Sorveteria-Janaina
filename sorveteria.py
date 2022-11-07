TR_P = 6.00
TR_M = 10.00
TR_G = 18.00
ES_P = 7.00
ES_M = 12.00
ES_G = 21.00
PR_P = 8.00
PR_M = 14.00
PR_G = 24.00
'''
    Classe: pedido tem como criar um classe para anotar e controlar os pedidos realizados
    
'''
class Pedidos:

    def verifi_tamanho(self,tamanho):
        if (tamanho == 'P' or tamanho == 'p'
                or tamanho == 'M' or tamanho == 'm'
                or tamanho == 'G' or tamanho == 'g'):
            if(tamanho == 'P'):
                return tamanho
            elif(tamanho == 'p'):
                return 'P'
            if(tamanho == 'M'):
                return tamanho
            elif(tamanho == 'm'):
                return 'M'
            if(tamanho == 'G'):
                return tamanho
            elif(tamanho == 'g'):
                return 'G'
        else:
            print('! ! ! ! !  TAMANHO ou CODIGO INVALIDO(S)')

    def verifi_codigo(self,codigo):
        if(codigo == 'TR' or codigo == 'tr'
            or codigo == 'ES' or codigo == 'es'
            or codigo == 'PR' or codigo == 'pr'):
            if(codigo == 'TR'):
                return codigo
            elif(codigo == 'tr'):
                return 'TR'
            if(codigo == 'ES'):
                return codigo
            elif(codigo == 'es'):
                return 'ES'
            if(codigo == 'PR'):
                return codigo
            elif(codigo == 'pr'):
                return 'PR'
        else:
            print('! ! ! ! !  TAMANHO ou CODIGO INVALIDO(S)')

    def set_tamanho(self, tamanho):
        self.tamanho = self.verifi_tamanho(tamanho)

    def set_codigo(self, codigo):
        self.codigo = self.verifi_codigo(codigo)

    def get_pedido(self):
        if(self.codigo == 'TR' and self.tamanho == 'P'):
            return TR_P
        if(self.codigo == 'TR' and self.tamanho == 'M'):
            return TR_M
        if (self.codigo == 'TR' and self.tamanho == 'G'):
            return TR_G
        if (self.codigo == 'ES' and self.tamanho == 'P'):
            return ES_P
        if (self.codigo == 'ES' and self.tamanho == 'G'):
            return ES_M
        if (self.codigo == 'PR' and self.tamanho == 'P'):
            return PR_P
        if (self.codigo == 'PR' and self.tamanho == 'P'):
            return PR_M
        if (self.codigo == 'PR' and self.tamanho == 'P'):
            return PR_G

    def get_tamanho(self):
        return self.tamanho
    def get_codigo(self):
        return self.codigo

class interface(Pedidos):

    def __int__(self):
        self.pedido = []
        self.control="S"
        while(True):
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

            if self.control== 'S' or self.control== 's':
                print('qwe')
            elif self.control== 'N' or self.control== 'n':
                print('qwe')
            else:
                print('qwe')


if __name__ == '__main__':
    print('sss')


