def cria_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, "titular": titular, "saldo": saldo, "limite":limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))


conta = cria_conta(123, "Gabriel", 600, 2000)

depositar(conta,100)

extrato(conta)
