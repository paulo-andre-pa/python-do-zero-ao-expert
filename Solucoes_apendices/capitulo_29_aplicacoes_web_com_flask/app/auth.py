import functools
import sqlite3
from flask import (Blueprint, flash, g, redirect, render_template_string,
                   request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.bd import obter

bp = Blueprint("auth", __name__, url_prefix="/auth")

FORMULARIO = """<h1>{{ titulo }}</h1>
{% for m in get_flashed_messages() %}<p>{{ m }}</p>{% endfor %}
<form method="post">
  <input name="nome" required> <input name="senha" type="password" required>
  <button>{{ titulo }}</button>
</form>"""

@bp.route("/registar", methods=["GET", "POST"])
def registar():
    if request.method == "POST":
        nome = request.form["nome"].strip()
        senha = request.form["senha"]
        if len(senha) < 8:
            flash("A palavra-passe deve ter pelo menos 8 carateres.")
        else:
            try:
                with obter() as bd:
                    bd.execute("INSERT INTO utilizadores (nome, hash) "
                               "VALUES (?, ?)",
                               (nome, generate_password_hash(senha)))
                return redirect(url_for("auth.entrar"))
            except sqlite3.IntegrityError:          # nome repetido (UNIQUE)
                flash(f"O utilizador {nome} já existe.")
    return render_template_string(FORMULARIO, titulo="Registar")

@bp.route("/entrar", methods=["GET", "POST"])
def entrar():
    if request.method == "POST":
        u = obter().execute("SELECT * FROM utilizadores WHERE nome = ?",
                            (request.form["nome"],)).fetchone()
        if u and check_password_hash(u["hash"], request.form["senha"]):
            session.clear()
            session["utilizador_id"] = u["id"]
            return redirect(url_for("tarefas.lista"))
        flash("Nome ou palavra-passe incorretos.")
    return render_template_string(FORMULARIO, titulo="Entrar")

@bp.route("/sair")
def sair():
    session.clear()
    return redirect(url_for("auth.entrar"))

@bp.before_app_request
def carregar_utilizador():
    uid = session.get("utilizador_id")
    g.utilizador = None if uid is None else obter().execute(
        "SELECT id, nome FROM utilizadores WHERE id = ?", (uid,)).fetchone()

def requer_sessao(vista):
    @functools.wraps(vista)
    def envolvente(**kwargs):
        if g.utilizador is None:
            return redirect(url_for("auth.entrar"))
        return vista(**kwargs)
    return envolvente
