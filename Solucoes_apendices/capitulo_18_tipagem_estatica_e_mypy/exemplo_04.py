# Capítulo 18 — Tipagem estática e mypy
# Secção: Tipos para estruturas de dados

from typing import TypedDict, NotRequired

class Morada(TypedDict):
    rua: str
    codigo_postal: str
    cidade: str

class Cliente(TypedDict):
    id: int
    nome: str
    morada: Morada
    telefone: NotRequired[str]     # chave opcional

m: Morada = {"rua": "Av. Central, 4", "codigo_postal": "4700-001",
            "cidade": "Braga"}
c: Cliente = {"id": 7, "nome": "Lúcia", "morada": m}
print(c["morada"]["cidade"], c.get("telefone", "sem telefone"))
