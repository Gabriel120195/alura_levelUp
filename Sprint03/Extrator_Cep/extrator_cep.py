import re

endereco = "Rua odila figueiredo nicolau, 222, selecta, São Bernardo do Campo, SP, 09791-520"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)