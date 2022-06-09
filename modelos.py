class Play_list:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas) 

    @property
    def listagem(self):
        return self._programas


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes =0
    
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} min - {self.likes} Likes"
      
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

        
    def __str__(self):
        return f"Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - {self.likes} Likes"
        

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('Todo mundo em panico', 1999, 100)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('demolidor', 2016, 2)


vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
minha_playlist = Play_list('fim de semana',filmes_e_series)

for programa in minha_playlist:
   print(programa)

print(f'Tamanho: {len(minha_playlist)}') 
