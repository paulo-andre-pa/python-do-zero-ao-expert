"""Gera um CSV de vendas fictício mas realista (com defeitos)."""
import numpy as np
import pandas as pd

PRODUTOS = {  # produto: (categoria, preço)
    "Ténis de corrida": ("Calçado", 89.9), "Chuteiras": ("Calçado", 69.9),
    "Bola de futebol": ("Equipamento", 24.9),
    "Raquete": ("Equipamento", 54.0),
    "Camisola técnica": ("Vestuário", 29.9), "Calções": ("Vestuário", 19.9),
    "Garrafa térmica": ("Acessórios", 14.5),
    "Mochila": ("Acessórios", 39.0),
}
LOJAS = {"Lisboa": 0.32, "Porto": 0.27, "Braga": 0.13, "Online": 0.28}

def gerar(n: int = 6000, semente: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(semente)
    datas = pd.to_datetime("2026-01-01") + pd.to_timedelta(
        rng.integers(0, 181, n), unit="D")
    # mais vendas ao fim de semana e na época de saldos (janeiro)
    peso = np.where(datas.dayofweek >= 5, 1.6, 1.0)
    peso *= np.where(datas.month == 1, 1.3, 1.0)
    idx = rng.choice(n, size=n, p=peso / peso.sum())
    produtos = rng.choice(list(PRODUTOS), n)
    datas = datas[idx]
    lojas = rng.choice(list(LOJAS), n, p=list(LOJAS.values()))
    # o canal online ganha peso todos os meses
    migra = rng.random(n) < 0.06 * (datas.month.to_numpy() - 1)
    lojas = np.where(migra, "Online", lojas)
    df = pd.DataFrame({
        "id_venda": np.arange(1, n + 1),
        "data": datas.strftime("%Y-%m-%d"),
        "loja": lojas,
        "produto": produtos,
        "categoria": [PRODUTOS[p][0] for p in produtos],
        "quantidade": rng.choice([1, 1, 1, 2, 2, 3], n),
        "preco_unit": [PRODUTOS[p][1] for p in produtos],
        "cliente": rng.zipf(1.6, n) % 900 + 1000,  # poucos compram muito
    })
    # defeitos típicos de exportações reais
    df.loc[rng.choice(n, 25), "loja"] = "lisboa "
    df.loc[rng.choice(n, 12), "quantidade"] = 0
    return pd.concat([df, df.sample(15, random_state=1)], ignore_index=True)
