from flask import Blueprint, abort, g, redirect, request, url_for
from app.auth import requer_sessao
from app.bd import obter

bp = Blueprint("tarefas", __name__)

@bp.route("/")
@requer_sessao
def lista():
    linhas = obter().execute(
        "SELECT id, titulo, feita FROM tarefas WHERE dono = ? ORDER BY id",
        (g.utilizador["id"],)).fetchall()
    itens = "".join(
        f"<li>{'[x]' if t['feita'] else '[ ]'} {t['titulo']}</li>"
        for t in linhas)
    return f"<p>Olá, {g.utilizador['nome']}</p><ul>{itens}</ul>"

@bp.post("/nova")
@requer_sessao
def nova():
    titulo = request.form.get("titulo", "").strip()
    if not titulo:
        abort(400)
    with obter() as bd:
        bd.execute("INSERT INTO tarefas (dono, titulo) VALUES (?, ?)",
                   (g.utilizador["id"], titulo))
    return redirect(url_for("tarefas.lista"))

@bp.post("/<int:tid>/feita")
@requer_sessao
def concluir(tid):
    with obter() as bd:
        cur = bd.execute("UPDATE tarefas SET feita = 1 "
                         "WHERE id = ? AND dono = ?",
                         (tid, g.utilizador["id"]))
    if cur.rowcount == 0:
        abort(404)
    return redirect(url_for("tarefas.lista"))
