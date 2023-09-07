pessoas = {
    "Gabriel" : 1,
    "Laura" : 2,
    "Nil" : 3,
    "Sandra" : 4,
    "Larissa" : 5
}

print(type(pessoas))

#Retorna o valor para aquela pessoa(String), no caso a chave é o nome
print(pessoas["Nil"])

#Se não tiver aquele valor, retorna 0
print(pessoas.get("aaa", 0))

#Se já tiver aquele valor, retorna seu valor
print(pessoas.get("Nil", 0))

#Adiciona elemento
pessoas["Carlos"] = 6
print(pessoas)

#Deleta elemento
del  pessoas["Gabriel"]
print(pessoas)

#Verifica se a chave esta no conjunto
print("Laura" in pessoas)

#intera sobre as chaves
for i in pessoas.keys():
    print(i)
#################################
#intera sobre seus valores
for i in pessoas.values():
    print(i)

#listando seus itens
for i in pessoas.items():
    print(i)

#ou melhor
for chave, valor in pessoas.items():
    print(chave, " = ", valor)

#Retornando em uma lista, as chaves
lista = ["Nomes: {}".format(chave) for chave in pessoas.keys()]
print(lista)