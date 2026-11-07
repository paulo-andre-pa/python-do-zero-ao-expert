# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Enumerações

from enum import Enum, auto

class Estado(Enum):
    PENDENTE = auto()
    PAGA = auto()
    ENVIADA = auto()
    ENTREGUE = auto()
    CANCELADA = auto()

TRANSICOES = {
    Estado.PENDENTE: {Estado.PAGA, Estado.CANCELADA},
    Estado.PAGA: {Estado.ENVIADA, Estado.CANCELADA},
    Estado.ENVIADA: {Estado.ENTREGUE},
}

def mudar(atual, novo):
    if novo not in TRANSICOES.get(atual, set()):
        raise ValueError(f"Transição inválida: {atual.name} -> {novo.name}")
    return novo

e = Estado.PENDENTE
e = mudar(e, Estado.PAGA)
e = mudar(e, Estado.ENVIADA)
print(e, e.name, e.value)
try:
    mudar(e, Estado.PENDENTE)
except ValueError as erro:
    print(erro)
