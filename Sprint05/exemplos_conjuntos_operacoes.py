usuarios = {1, 7, 10, 25, 40, 32, 5, 50, 75}
print(len(usuarios))

#adicionando elementos caso não esteja no conjunto
usuarios.add(90)
print(len(usuarios))

#congela os conjuntos para não permitir adicionar
usuarios_congelados = frozenset(usuarios)
print(type(usuarios_congelados))

meu_texto = "Bem vindo meu nome é gabriel tenho 2 gatos meus gatos se chamam marios e marisca o marios é branco e a marisca preta"
print(meu_texto.split())

#Removendo a duplicidade do texto
print(set(meu_texto.split()))
