# Capítulo 23 — Redes, HTTP e APIs web
# Secção: A biblioteca requests

import requests

r = requests.post(f"{BASE}/tarefas", json={"titulo": "Preparar reunião"},
                  timeout=5)
print(r.status_code, r.json())
r = requests.get(f"{BASE}/tarefas", timeout=5)
r.raise_for_status()                 # lança exceção se 4xx/5xx
print([t["titulo"] for t in r.json()])
print(r.headers["Content-Type"])
