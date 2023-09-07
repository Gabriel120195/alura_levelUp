meu_texto = "Bem vindo meu nome é gabriel tenho 2 gatos meus gatos se chamam Marios e Marisca o Marios é branco e a Marisca preta"

#Transforma o texto em minusculo
meu_texto_minus = meu_texto.lower()
print(meu_texto_minus)

#Retorna as aparicoes daquela palavra no texto
aparicoes = {}
for palavra in meu_texto_minus.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)
