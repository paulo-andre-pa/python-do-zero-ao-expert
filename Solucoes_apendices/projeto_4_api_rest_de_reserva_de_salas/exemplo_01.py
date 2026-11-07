# Projeto 4 — API REST de reserva de salas
# Secção: Utilização

import os, sys, threading, json, urllib.request, urllib.error
sys.path.insert(0, os.path.abspath("src"))
from wsgiref.simple_server import make_server, WSGIRequestHandler
from reservas.api import criar_app
from reservas.servidor import preparar

class Silencioso(WSGIRequestHandler):
    def log_message(self, *args):
        pass

srv = make_server("127.0.0.1", 0, criar_app(preparar(":memory:")),
                  handler_class=Silencioso)
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{srv.server_port}"

def http(metodo, caminho, corpo=None):
    dados = json.dumps(corpo).encode() if corpo else None
    req = urllib.request.Request(URL + caminho, data=dados, method=metodo)
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            texto = r.read().decode()
            return r.status, json.loads(texto) if texto else ""
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())

def reservar(sala, quem, n, inicio, fim):
    return http("POST", "/reservas", {
        "sala_id": sala, "responsavel": quem, "participantes": n,
        "inicio": inicio, "fim": fim})

print(http("GET", "/salas")[1][:3])
QUA, SAB = "2026-06-03T", "2026-06-06T"      # quarta e sábado
print(reservar(2, "Startup Lume", 5, QUA + "14:00", QUA + "16:00"))
print(reservar(2, "Ana", 3, QUA + "15:00", QUA + "15:30"))
print(reservar(1, "Rui", 2, SAB + "10:00", SAB + "11:00"))
print(http("GET", "/disponiveis?inicio=2026-06-03T15:00"
                  "&fim=2026-06-03T16:00&pessoas=5"))
print(http("GET", "/salas/2/reservas?dia=2026-06-03")[1][0]["responsavel"])
srv.shutdown()
