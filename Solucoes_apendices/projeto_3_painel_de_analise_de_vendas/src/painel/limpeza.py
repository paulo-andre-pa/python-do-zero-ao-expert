"""Leitura, validação e limpeza dos dados de vendas."""
import logging
import pandas as pd

log = logging.getLogger(__name__)
COLUNAS = {"id_venda", "data", "loja", "produto", "categoria",
           "quantidade", "preco_unit", "cliente"}

class FicheiroInvalido(ValueError):
    pass

def ler(caminho) -> pd.DataFrame:
    df = pd.read_csv(caminho, parse_dates=["data"])
    em_falta = COLUNAS - set(df.columns)
    if em_falta:
        raise FicheiroInvalido(f"colunas em falta: {sorted(em_falta)}")
    log.info("lidas %d linhas", len(df))
    return df

def limpar(df: pd.DataFrame) -> pd.DataFrame:
    n0 = len(df)
    df = df.drop_duplicates(subset="id_venda")
    log.info("removidos %d duplicados", n0 - len(df))
    invalidas = df["quantidade"] <= 0
    log.info("removidas %d linhas com quantidade inválida", invalidas.sum())
    def canal(d):
        return d["loja"].where(d["loja"] == "Online", "Física")

    return (df.loc[~invalidas]
              .assign(loja=lambda d: d["loja"].str.strip().str.title(),
                      total=lambda d: d["quantidade"] * d["preco_unit"],
                      canal=canal,
                      mes=lambda d: d["data"].dt.to_period("M"))
              .reset_index(drop=True))
