"""API REST de tarefas, apenas com a biblioteca padrão."""
import json
import re
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

TAREFAS: dict[int, dict] = {}
PROXIMO_ID = 1
NAO_ENCONTRADA = {"erro": "não encontrada"}

class Handler(BaseHTTPRequestHandler):
    def _responder(self, estado, corpo=None):
        dados = json.dumps(corpo, ensure_ascii=False).encode()
        self.send_response(estado)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(dados)))
        self.end_headers()
        self.wfile.write(dados)

    def _ler_json(self):
        tamanho = int(self.headers.get("Content-Length", 0))
        try:
            return json.loads(self.rfile.read(tamanho) or b"{}")
        except json.JSONDecodeError:
            return None

    def _id_do_caminho(self):
        m = re.fullmatch(r"/tarefas/(\d+)", self.path)
        return int(m.group(1)) if m else None

    def do_GET(self):
        if self.path == "/tarefas":
            return self._responder(HTTPStatus.OK, list(TAREFAS.values()))
        tid = self._id_do_caminho()
        if tid in TAREFAS:
            return self._responder(HTTPStatus.OK, TAREFAS[tid])
        self._responder(HTTPStatus.NOT_FOUND, NAO_ENCONTRADA)

    def do_POST(self):
        global PROXIMO_ID
        if self.path != "/tarefas":
            return self._responder(HTTPStatus.NOT_FOUND, {"erro": "rota"})
        dados = self._ler_json()
        if not dados or not str(dados.get("titulo", "")).strip():
            return self._responder(HTTPStatus.BAD_REQUEST,
                                   {"erro": "campo 'titulo' obrigatório"})
        tarefa = {"id": PROXIMO_ID, "titulo": dados["titulo"].strip(),
                  "feita": False}
        TAREFAS[PROXIMO_ID] = tarefa
        PROXIMO_ID += 1
        self._responder(HTTPStatus.CREATED, tarefa)

    def do_PATCH(self):
        tid, dados = self._id_do_caminho(), self._ler_json()
        if tid not in TAREFAS:
            return self._responder(HTTPStatus.NOT_FOUND, NAO_ENCONTRADA)
        if "feita" in (dados or {}):
            TAREFAS[tid]["feita"] = bool(dados["feita"])
        self._responder(HTTPStatus.OK, TAREFAS[tid])

    def do_DELETE(self):
        tid = self._id_do_caminho()
        if TAREFAS.pop(tid, None) is None:
            return self._responder(HTTPStatus.NOT_FOUND, NAO_ENCONTRADA)
        self._responder(HTTPStatus.NO_CONTENT)

    def log_message(self, *args):        # silencia o registo por omissão
        pass

def criar_servidor(porta=8000):
    return ThreadingHTTPServer(("127.0.0.1", porta), Handler)

if __name__ == "__main__":
    print("API em http://127.0.0.1:8000/tarefas")
    criar_servidor().serve_forever()
