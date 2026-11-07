"""Regras de negócio da triagem (independentes do modelo concreto)."""
import re
from dataclasses import dataclass
from typing import Protocol

from triagem.modelo import normalizar

class Classificador(Protocol):
    classes_: list[str]
    def predict_proba(self, textos: list[str]): ...

EQUIPAS = {"faturacao": ("Faturação", 24),
           "tecnico": ("Assistência técnica", 8),
           "entregas": ("Logística", 24),
           "conta": ("Gestão de conta", 48)}

URGENTE = re.compile(
    r"\b(sem (internet|servico|sinal|net) (ha|desde)"
    r"|nao (tenho|funciona) (nada|nenhum servico)"
    r"|(vou|quero) (cancelar|rescindir) (o )?(contrato|servico|tudo)"
    r"|mudar de operador|deco|livro de reclamacoes)\b")

@dataclass(frozen=True)
class Decisao:
    categoria: str
    confianca: float
    equipa: str
    prazo_horas: int
    urgente: bool
    manual: bool

class Triagem:
    def __init__(self, classificador: Classificador, limiar: float = 0.6):
        if not 0 < limiar < 1:
            raise ValueError("o limiar tem de estar entre 0 e 1")
        self.classificador = classificador
        self.limiar = limiar

    def classificar(self, texto: str) -> Decisao:
        if not texto.strip():
            raise ValueError("pedido vazio")
        probs = self.classificador.predict_proba([texto])[0]
        melhor = max(range(len(probs)), key=lambda i: probs[i])
        categoria = self.classificador.classes_[melhor]
        confianca = float(probs[melhor])
        urgente = bool(URGENTE.search(normalizar(texto)))
        manual = confianca < self.limiar
        if manual:
            equipa, prazo = "Triagem manual", 4
        else:
            equipa, prazo = EQUIPAS[categoria]
        if urgente:
            prazo = min(prazo, 2)
        return Decisao(categoria, round(confianca, 3), equipa, prazo,
                       urgente, manual)
