idades = [39, 10, 27, 18]

#tipo
print(type(idades))

#tamanho
print(len(idades))

#adicionar valor
idades.append(5)
print(idades)

#adiciona elemento na posição desejada
idades.insert(0,28)
print(idades)

#adicionando varios elementos
idades.extend([60,75])
print(idades)

#remove valor
idades.remove(10)
print(idades)

#verifica se tem elemento
print(39 in idades)

#imprime todas idades
for idade in idades:
    print(idade)

#adicionando +1 na idade modo antigo
idades_mais_um = []
for idade in idades:
    idades_mais_um.append(idade+1)
print(idades_mais_um)

#adicionando +1 na idade modo novo
idades_mais_um_novo = [(idade+1) for idade in idades]
print(idades_mais_um_novo)

#filtrando elementos
lista_filtrada = [(idade) for idade in idades if idade > 30]
print(lista_filtrada)










