# Capítulo 23 — Redes, HTTP e APIs web
# Secção: Consumir APIs com urllib

import json, threading
import urllib.request, urllib.error
from api_tarefas import criar_servidor

servidor = criar_servidor(porta=0)            # 0: escolhe uma porta livre
porta = servidor.server_address[1]
threading.Thread(target=servidor.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{porta}"

def pedido(metodo, caminho, corpo=None):
    dados = json.dumps(corpo).encode() if corpo is not None else None
    cabecalhos = {"Content-Type": "application/json"}
    req = urllib.request.Request(BASE + caminho, data=dados,
                                 method=metodo, headers=cabecalhos)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            texto = resp.read().decode()
            return resp.status, json.loads(texto) if texto else None
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode())

print(pedido("POST", "/tarefas", {"titulo": "Rever contrato"}))
print(pedido("POST", "/tarefas", {"titulo": "Pagar fornecedores"}))
print(pedido("POST", "/tarefas", {"titulo": "   "}))
print(pedido("PATCH", "/tarefas/1", {"feita": True}))
print(pedido("DELETE", "/tarefas/2"))
print(pedido("GET", "/tarefas"))
print(pedido("GET", "/tarefas/99"))
