"""Uso: python -m painel vendas.csv relatorio.html"""
import logging
import sys
from pathlib import Path

from painel import graficos, indicadores as ind, limpeza, relatorio

log = logging.getLogger("painel")

def main(argv: list[str]) -> int:
    logging.basicConfig(level=logging.WARNING, stream=sys.stdout,
                        format="%(levelname)s %(message)s", force=True)
    log.setLevel(logging.INFO)
    entrada, saida = Path(argv[0]), Path(argv[1])
    df = limpeza.limpar(limpeza.ler(entrada))
    lojas = ind.por_loja(df)
    html = relatorio.gerar_html(
        "Relatório de vendas — 1.º semestre 2026",
        ind.comparar_ultimo_mes(df), lojas, ind.top_produtos(df),
        ind.clientes(df),
        [graficos.evolucao_mensal(ind.mensal(df)),
         graficos.barras_lojas(lojas)])
    saida.write_text(html, encoding="utf-8")
    log.info("relatório gravado em %s (%d KB)", saida,
             saida.stat().st_size // 1024)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
