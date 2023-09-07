usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(set(assistiram))

for usuario in assistiram:
    print(usuario)

#iniciando conjuntos
usuarios_data_science_conjuntos = {15, 23, 43, 56}
usuarios_machine_learning_conjuntos = {13, 23, 56, 42}

#Esta em um ou outro
print(usuarios_machine_learning_conjuntos | usuarios_data_science_conjuntos)

#Esta em um e no outro
print(usuarios_machine_learning_conjuntos & usuarios_data_science_conjuntos)

#Esta em um - oq esta no outro
print(usuarios_machine_learning_conjuntos - usuarios_data_science_conjuntos)

#consultando os conjuntos
fez_ds_mas_nao_fez_ml = usuarios_data_science_conjuntos - usuarios_machine_learning_conjuntos
print(15 in fez_ds_mas_nao_fez_ml)