from operator import attrgetter
from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<".format(self._codigo, self._saldo)



conta_gabriel = ContaSalario(222)
conta_gabriel.deposita(500)

conta_laura = ContaSalario(111)
conta_laura.deposita(1000)

conta_sandra = ContaSalario(333)
conta_sandra.deposita(1000)


contas = [conta_laura, conta_gabriel, conta_sandra]

for conta in contas:
    print(conta)

#criando ordenação
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

print(conta_gabriel < conta_sandra)


for conta in sorted(contas, reverse=True):
    print(conta)


