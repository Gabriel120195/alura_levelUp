from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError
from leitor import LeitorDeArquivo
class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidos = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas


    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O atributo agencia deve ser um inteiro", valor)

        if valor <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")

        self.__agencia = valor

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O atributo numero deve ser um inteiro")
        if valor <= 0:
            raise ValueError("O atributo numero deve ser maior que zero")

        self.__numero = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O atributo saldo deve ser um inteiro")

        self.__saldo = valor

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero!")
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidos += 1
            E.args = ()
            raise OperacaoFinanceiraError("Operação não finalizada") from E
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero!")
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError('', self.saldo, valor)
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor



def main():
    import sys

    contas =[]
    while(True):
        try:
            nome = input("Nome do cliente: \n")
            agencia = input("Número da agência: \n")
            breakpoint()
            numero = input("Número da conta corrente: \n")

            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append = conta_corrente
        except KeyboardInterrupt:
            print(f"\n\n {len(contas)} conta(s) criadas")
            sys.exit()

# if __name__ == "__main__":
#     main()


# conta01 = ContaCorrente(None, 400, 1234567)
# conta02 = ContaCorrente(None, 650, 9871456)
#
# try:
#     conta01.sacar(1000)
#     conta01.transferir(1000, conta02)
#     print(conta01.saldo)
#     print(conta02.saldo)
# except OperacaoFinanceiraError as E:
#     breakpoint()
#     pass

with LeitorDeArquivo("arquivo.txt") as leitor:
    leitor.ler_proxima_linha()