"""Persistência das tarefas em SQLite."""
import sqlite3
from datetime import date

from tarefas.modelos import Prioridade, Tarefa

ESQUEMA = """
CREATE TABLE IF NOT EXISTS tarefas (
    id         INTEGER PRIMARY KEY,
    titulo     TEXT    NOT NULL,
    prioridade INTEGER NOT NULL,
    prazo      TEXT,
    etiquetas  TEXT    NOT NULL DEFAULT '',
    concluida  INTEGER NOT NULL DEFAULT 0
)"""

class RepositorioTarefas:
    def __init__(self, caminho: str = ":memory:") -> None:
        self.con = sqlite3.connect(caminho)
        self.con.row_factory = sqlite3.Row
        self.con.execute(ESQUEMA)

    @staticmethod
    def _para_tarefa(linha: sqlite3.Row) -> Tarefa:
        prazo, etiquetas = linha["prazo"], linha["etiquetas"]
        return Tarefa(
            titulo=linha["titulo"],
            prioridade=Prioridade(linha["prioridade"]),
            prazo=date.fromisoformat(prazo) if prazo else None,
            etiquetas=etiquetas.split(",") if etiquetas else [],
            concluida=bool(linha["concluida"]),
            id=linha["id"],
        )

    def guardar(self, t: Tarefa) -> Tarefa:
        valores = (t.titulo, int(t.prioridade),
                   t.prazo.isoformat() if t.prazo else None,
                   ",".join(t.etiquetas), int(t.concluida))
        with self.con:
            if t.id is None:
                cur = self.con.execute(
                    "INSERT INTO tarefas (titulo, prioridade, prazo, "
                    "etiquetas, concluida) VALUES (?, ?, ?, ?, ?)", valores)
                t.id = cur.lastrowid
            else:
                self.con.execute(
                    "UPDATE tarefas SET titulo = ?, prioridade = ?, "
                    "prazo = ?, etiquetas = ?, concluida = ? WHERE id = ?",
                    (*valores, t.id))
        return t

    def obter(self, id_: int) -> Tarefa | None:
        linha = self.con.execute("SELECT * FROM tarefas WHERE id = ?",
                                 (id_,)).fetchone()
        return self._para_tarefa(linha) if linha else None

    def todas(self) -> list[Tarefa]:
        linhas = self.con.execute(
            "SELECT * FROM tarefas ORDER BY concluida, prioridade, "
            "prazo IS NULL, prazo, id")
        return [self._para_tarefa(l) for l in linhas]

    def apagar(self, id_: int) -> bool:
        with self.con:
            cur = self.con.execute("DELETE FROM tarefas WHERE id = ?",
                                   (id_,))
        return cur.rowcount == 1
