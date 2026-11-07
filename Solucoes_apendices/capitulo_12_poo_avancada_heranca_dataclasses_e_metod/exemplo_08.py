# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Métodos especiais (dunder)

class Playlist:
    def __init__(self, nome, musicas):
        self.nome = nome
        self._musicas = list(musicas)

    def __len__(self):
        return len(self._musicas)

    def __getitem__(self, indice):
        return self._musicas[indice]

p = Playlist("Estrada", ["Rio", "Vento", "Mar", "Serra"])
print(len(p), p[0], p[-1], p[1:3], "Mar" in p)
for i, m in enumerate(p, 1):
    print(i, m, end=" | ")
print()
