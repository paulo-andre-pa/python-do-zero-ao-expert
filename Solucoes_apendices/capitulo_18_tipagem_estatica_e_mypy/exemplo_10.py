# Capítulo 18 — Tipagem estática e mypy
# Secção: Outras ferramentas úteis

from typing import Self, overload, cast, assert_never
from enum import Enum

class Construtor:
    def __init__(self) -> None:
        self.partes: list[str] = []
    def com(self, parte: str) -> Self:      # devolve a própria classe
        self.partes.append(parte)
        return self

print(Construtor().com("motor").com("rodas").partes)

class Cor(Enum):
    VERMELHO = 1
    VERDE = 2

def nome_cor(c: Cor) -> str:
    match c:
        case Cor.VERMELHO:
            return "vermelho"
        case Cor.VERDE:
            return "verde"
        case _:
            assert_never(c)   # o verificador avisa se faltar um caso

print(nome_cor(Cor.VERDE))
