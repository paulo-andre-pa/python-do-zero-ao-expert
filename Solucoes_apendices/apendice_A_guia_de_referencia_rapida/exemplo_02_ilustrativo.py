# Apêndice A — Guia de referência rápida
# Secção: Funções e classes
# Exemplo ilustrativo: pode exigir pacotes ou serviços externos.

def f(pos, /, normal, *args, chave=1, **kwargs) -> tipo: ...

lambda x: x * 2

@decorador
def g(): ...

class Classe(Base):
    atributo_de_classe = 0
    def __init__(self, x): super().__init__(); self.x = x
    def __repr__(self): return f"Classe({self.x!r})"
    @property
    def dobro(self): return 2 * self.x
    @classmethod
    def criar(cls, texto): return cls(int(texto))
    @staticmethod
    def utilitario(v): return v

@dataclass(frozen=True, order=True, slots=True)
class Ponto:
    x: float
    y: float = 0.0
    etiquetas: list[str] = field(default_factory=list)
