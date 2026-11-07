"""Geração do relatório HTML autónomo."""
import base64
import io
from html import escape

def _imagem(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150)
    dados = base64.b64encode(buf.getvalue()).decode()
    return f'<img src="data:image/png;base64,{dados}" alt="gráfico">'

def _fmt_var(v) -> str:
    return "—" if v is None else f"{v:+.1%}"

def gerar_html(titulo: str, comparacao: dict, lojas, produtos, cli,
               figuras: list) -> str:
    cartoes = "".join(
        f"<div class='kpi'><b>{escape(k.replace('_', ' '))}</b>"
        f"<span>{v:,.2f}</span><small>{_fmt_var(var)}</small></div>"
        for k, (v, var) in comparacao.items())
    tabela_lojas = lojas.to_html(float_format="{:,.2f}".format,
                                 classes="tabela")
    lista = "".join(f"<li>{escape(p)}: {v:,.2f} €</li>"
                    for p, v in produtos.items())
    graficos = "".join(_imagem(f) for f in figuras)
    return f"""<!doctype html>
<html lang="pt"><head><meta charset="utf-8"><title>{escape(titulo)}</title>
<style>body{{font-family:sans-serif;max-width:900px;margin:auto}}
.kpi{{display:inline-block;border:1px solid #999;padding:8px;margin:4px}}
.kpi span{{display:block;font-size:1.4em}} img{{max-width:100%}}</style>
</head><body><h1>{escape(titulo)}</h1>
<h2>Último mês face ao anterior</h2>{cartoes}
<h2>Evolução e lojas</h2>{graficos}{tabela_lojas}
<h2>Top produtos</h2><ol>{lista}</ol>
<h2>Clientes</h2><p>{cli['recorrentes']:.0%} dos clientes compraram mais
de uma vez; {cli['pct_clientes_80pct']:.0%} dos clientes geram 80 % da
faturação.</p></body></html>"""
