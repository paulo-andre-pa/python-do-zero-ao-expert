# Capítulo 27 — Padrões de projeto e arquitetura
# Secção: Command: operações como objetos

from dataclasses import dataclass, field

@dataclass
class Documento:
    texto: str = ""

@dataclass
class Inserir:
    posicao: int
    conteudo: str
    def executar(self, doc: Documento):
        t, p = doc.texto, self.posicao
        doc.texto = t[:p] + self.conteudo + t[p:]
    def desfazer(self, doc: Documento):
        fim = self.posicao + len(self.conteudo)
        doc.texto = doc.texto[:self.posicao] + doc.texto[fim:]

@dataclass
class Editor:
    doc: Documento = field(default_factory=Documento)
    feitos: list = field(default_factory=list)
    desfeitos: list = field(default_factory=list)

    def fazer(self, comando):
        comando.executar(self.doc)
        self.feitos.append(comando)
        self.desfeitos.clear()

    def anular(self):
        comando = self.feitos.pop()
        comando.desfazer(self.doc)
        self.desfeitos.append(comando)

    def refazer(self):
        comando = self.desfeitos.pop()
        comando.executar(self.doc)
        self.feitos.append(comando)

ed = Editor()
ed.fazer(Inserir(0, "Olá"))
ed.fazer(Inserir(3, " mundo"))
print(repr(ed.doc.texto))
ed.anular();  print(repr(ed.doc.texto))
ed.refazer(); print(repr(ed.doc.texto))
