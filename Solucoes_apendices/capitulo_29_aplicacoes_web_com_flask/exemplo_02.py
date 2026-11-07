# Capítulo 29 — Aplicações web com Flask
# Secção: Modelos HTML com Jinja2

import os
from flask import Flask, render_template

app = Flask(__name__, template_folder=os.path.abspath("templates"))

@app.route("/")
def inicio():
    return "Início"

@app.route("/produtos")
def produtos():
    lista = [{"nome": "Mochila", "preco": 39.9},
             {"nome": "Tenda <2 pessoas>", "preco": 129.0}]
    return render_template("produtos.html", produtos=lista)

html = app.test_client().get("/produtos").get_data(as_text=True)
print("\n".join(l.strip() for l in html.splitlines()
                if "<li>" in l or "<h1>" in l or "strong" in l))
