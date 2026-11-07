# Capítulo 23 — Redes, HTTP e APIs web
# Secção: A biblioteca requests
# Exemplo ilustrativo: pode exigir pacotes ou serviços externos.

import os, requests

sessao = requests.Session()           # reutiliza ligações e cabeçalhos
sessao.headers["Authorization"] = f"Bearer {os.environ['CHAVE_API']}"

resp = sessao.get("https://api.exemplo.com/v1/encomendas",
                  params={"estado": "pendente", "pagina": 1},
                  timeout=10)
resp.raise_for_status()
for encomenda in resp.json()["resultados"]:
    print(encomenda["id"], encomenda["total"])
