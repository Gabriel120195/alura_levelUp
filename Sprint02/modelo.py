class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} Min - {self._likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} Temp - {self._likes} Likes"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)
    
    def __getitem__(self, item):
        return self._programas[item]



oGangster = Filme("o gângster", 2007, 180)
oGangster.dar_likes()
oGangster.dar_likes()

gladiador = Filme("Gladiador", 2000, 120)
gladiador.dar_likes()
gladiador.dar_likes()
gladiador.dar_likes()
gladiador.dar_likes()
gladiador.dar_likes()
gladiador.dar_likes()

breakingBad = Serie("breaking bad", 2008, 5)
breakingBad.dar_likes()
breakingBad.dar_likes()
breakingBad.dar_likes()
breakingBad.dar_likes()


csi = Serie("Csi - Las vegas", 2000, 15)
csi.dar_likes()
csi.dar_likes()
csi.dar_likes()

filmes_e_series = [oGangster, breakingBad, gladiador, csi]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f"Tamanho do playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)
