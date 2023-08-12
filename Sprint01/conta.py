
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transferencia(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, valor):
        self.__limite = valor
    @staticmethod
    def codigo_banco():
        return "001"
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}


conta = Conta(numero=1234, titular="gabriel", saldo=100, limite=2500)
conta2 = Conta(numero= 1111, titular="luis", saldo=500, limite=10000)