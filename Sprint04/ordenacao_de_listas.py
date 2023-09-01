
idades = [20, 31, 45, 10, 5, 68, 75]

for i in range(len(idades)):
    print(i, idades[i])

print(list(range(len(idades))))
print(list(enumerate(idades)))

for i in enumerate(idades):
    print(i)

for indice,idade in enumerate(idades):
    print(indice, "x", idade)

usuarios = [
    ("Gabriel", 28, 1995),
    ("Laura", 2, 2021),
    ("Sandra", 51, 1972)
    ]

for nome, idade, ano in usuarios:
    print(nome)

print(sorted(idades))
print(sorted(idades, reverse=True))

