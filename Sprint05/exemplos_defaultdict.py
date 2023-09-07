from collections import defaultdict
from collections import Counter

meu_texto = "Bem vindo meu nome é gabriel tenho 2 gatos meus gatos se chamam Marios e Marisca o Marios é branco e a Marisca preta"

#Transforma o texto em minusculo
meu_texto_minus = meu_texto.lower()
print(meu_texto_minus)

aparicoes = defaultdict(int)

for palavra in meu_texto_minus.split():
    aparicoes[palavra] += 1

print(aparicoes)
#############################################
#outro exemplo

class Conta:
    def __init__(self):
        print("Criando conta...")

contas = defaultdict(Conta)
contas[15]

#############################################
#Utilizando o import contador
aparicoes_contador = Counter(meu_texto.split())
print(aparicoes_contador)







