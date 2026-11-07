import pandas as pd
import pytest
from painel import indicadores as ind
from painel.limpeza import limpar

@pytest.fixture
def df():
    bruto = pd.DataFrame({
        "id_venda": [1, 2, 3, 4, 4, 5],
        "data": pd.to_datetime(["2026-01-10", "2026-01-12", "2026-02-03",
                                "2026-02-05", "2026-02-05", "2026-02-07"]),
        "loja": ["Porto", "porto ", "Online", "Porto", "Porto", "Online"],
        "produto": ["A", "B", "A", "B", "B", "A"],
        "categoria": ["X"] * 6,
        "quantidade": [1, 2, 1, 1, 1, 0],
        "preco_unit": [10.0, 5.0, 10.0, 30.0, 30.0, 10.0],
        "cliente": [1, 2, 1, 3, 3, 4],
    })
    return limpar(bruto)

def test_limpeza(df):
    assert len(df) == 4                      # 1 duplicado, 1 quantidade 0
    assert set(df["loja"]) == {"Porto", "Online"}
    assert set(df["canal"]) == {"Física", "Online"}

def test_kpis(df):
    assert ind.kpis(df) == {"faturacao": 60.0, "vendas": 4,
                            "ticket_medio": 15.0, "clientes": 3}

def test_comparacao_mensal(df):
    comp = ind.comparar_ultimo_mes(df)
    assert comp["faturacao"] == (40.0, pytest.approx(1.0))   # 20 -> 40

def test_variacao_sem_base():
    assert ind.variacao(10, 0) is None

def test_por_loja_quotas_somam_1(df):
    assert ind.por_loja(df)["quota"].sum() == pytest.approx(1.0)

def test_top_produtos(df):
    assert list(ind.top_produtos(df, 1).index) == ["B"]

def test_clientes(df):
    c = ind.clientes(df)
    assert c["recorrentes"] == pytest.approx(1 / 3, abs=1e-3)
    assert c["clientes_80pct"] == 2
