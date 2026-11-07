# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: JSON

import json
from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class Fatura:
    numero: str
    cliente: str
    data: date
    total: float

def codificar(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Tipo não serializável: {type(obj).__name__}")

faturas = [Fatura("FT 2026/41", "Loja Central", date(2026, 3, 2), 412.5),
           Fatura("FT 2026/42", "Café Avenida", date(2026, 3, 4), 89.0)]
texto = json.dumps([asdict(f) for f in faturas], default=codificar,
                   ensure_ascii=False)
print(texto)

def para_fatura(d):
    return Fatura(**{**d, "data": date.fromisoformat(d["data"])})

recuperadas = [para_fatura(d) for d in json.loads(texto)]
print(recuperadas[0].data.strftime("%d/%m/%Y"), recuperadas == faturas)
