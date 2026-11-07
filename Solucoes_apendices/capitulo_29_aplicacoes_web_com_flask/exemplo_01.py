# Capítulo 29 — Aplicações web com Flask
# Secção: A primeira aplicação

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Olá, Flask!</h1>"

@app.route("/saudar/<nome>")
def saudar(nome):
    vezes = request.args.get("vezes", 1, type=int)
    return f"Olá, {nome}! " * vezes

@app.route("/api/estado")
def estado():
    return jsonify(servico="ok", versao="1.0")

cliente = app.test_client()             # simula um navegador
r = cliente.get("/saudar/Ana?vezes=2")
print(r.status_code, r.get_data(as_text=True))
print(cliente.get("/api/estado").get_json())
print(cliente.get("/inexistente").status_code)
