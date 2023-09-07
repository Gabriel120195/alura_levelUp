from collections import Counter
texto1 = """
Python é uma linguagem de programação versátil e poderosa que tem ganhado cada vez mais popularidade
ao longo dos anos. Criada por Guido van Rossum e lançada pela primeira vez em 1991, Python foi projetada 
com o objetivo de ser uma linguagem de programação de alto nível, fácil de ler e escrever. 
Desde então, ela se tornou uma das linguagens mais utilizadas em uma ampla variedade de aplicações, 
desde desenvolvimento web até aprendizado de máquina e análise de dados.
Uma das características mais distintas do Python é a sua sintaxe clara e legível, que se assemelha muito ao inglês, 
tornando-a uma excelente escolha para programadores iniciantes. O código em Python é estruturado por meio de 
indentação, o que o torna fácil de ler e entender, promovendo a escrita de código limpo e organizado.
"""

texto2 = """
Python é uma linguagem de programação versátil e poderosa que tem ganhado cada vez mais popularidade ao longo 
dos anos. Criada por Guido van Rossum e lançada pela primeira vez em 1991, Python foi projetada com o objetivo 
de ser uma linguagem de programação de alto nível, fácil de ler e escrever. Desde então, ela se tornou uma 
das linguagens mais utilizadas em uma ampla variedade de aplicações, desde desenvolvimento web até aprendizado 
de máquina e análise de dados.
Uma das características mais distintas do Python é a sua sintaxe clara e legível, que se assemelha muito ao inglês, 
tornando-a uma excelente escolha para programadores iniciantes. O código em Python é estruturado por meio de 
indentação, o que o torna fácil de ler e entender, promovendo a escrita de código limpo e organizado.
"""
def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto1.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(texto1)