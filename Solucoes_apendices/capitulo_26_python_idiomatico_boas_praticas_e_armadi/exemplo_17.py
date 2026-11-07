# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Lista de verificação para revisões de código

from dataclasses import dataclass

@dataclass(frozen=True)
class Linha:
    nome: str
    saldo: float

def linhas_ativas(dados: list[dict]) -> list[Linha]:
    linhas = []
    for registo in dados:
        if not registo.get("ativo"):
            continue
        try:
            saldo = float(registo["saldo"])
        except (KeyError, TypeError, ValueError):
            continue        # sem saldo válido: ignorado de propósito
        linhas.append(Linha(registo["nome"].strip().title(), saldo))
    return linhas

def relatorio_novo(dados: list[dict], separador: str = ",") -> str:
    return "".join(f"{l.nome}{separador}{l.saldo:.2f}\n"
                   for l in linhas_ativas(dados))

amostra = [{"nome": " ana ", "saldo": "10.5", "ativo": True},
           {"nome": "rui", "saldo": "x", "ativo": True},
           {"nome": "eva", "saldo": 3, "ativo": False}]
print(repr(relatorio_novo(amostra)))
print(relatorio(amostra) == relatorio_novo(amostra))
