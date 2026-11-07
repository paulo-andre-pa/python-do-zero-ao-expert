# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Introspeção

import inspect

def calcular_juros(capital: float, taxa: float = 0.03, *,
                   anos: int) -> float:
    """Juros compostos."""
    return capital * (1 + taxa) ** anos

assinatura = inspect.signature(calcular_juros)
for nome, p in assinatura.parameters.items():
    tipo = p.annotation.__name__
    print(f"{nome:<8} omissão={p.default!r:<12} tipo={tipo}")
print(assinatura.return_annotation, inspect.getdoc(calcular_juros))
print(hasattr(Produto, "preco"), callable(calcular_juros))
print([n for n in dir(Produto) if not n.startswith("_")])
