# Capítulo 18 — Tipagem estática e mypy
# Secção: Genéricos

from dataclasses import dataclass, field

@dataclass
class Pilha[T]:
    _itens: list[T] = field(default_factory=list)

    def empilhar(self, item: T) -> None:
        self._itens.append(item)

    def desempilhar(self) -> T:
        if not self._itens:
            raise IndexError("pilha vazia")
        return self._itens.pop()

    def __len__(self) -> int:
        return len(self._itens)

p: Pilha[str] = Pilha()
p.empilhar("abrir ficheiro")
p.empilhar("editar texto")
print(p.desempilhar(), len(p))
