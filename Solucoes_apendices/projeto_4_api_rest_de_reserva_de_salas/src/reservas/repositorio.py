"""Acesso a dados em SQLite."""
import sqlite3
from datetime import date, datetime

ESQUEMA = """
CREATE TABLE IF NOT EXISTS salas (
    id INTEGER PRIMARY KEY, nome TEXT NOT NULL,
    capacidade INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY,
    sala_id INTEGER NOT NULL REFERENCES salas(id),
    responsavel TEXT NOT NULL, participantes INTEGER NOT NULL,
    inicio TEXT NOT NULL, fim TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS idx_reservas ON reservas (sala_id, inicio);
"""

class Repositorio:
    def __init__(self, caminho: str = ":memory:") -> None:
        self.con = sqlite3.connect(caminho, check_same_thread=False)
        self.con.row_factory = sqlite3.Row
        self.con.executescript(ESQUEMA)

    def criar_sala(self, nome: str, capacidade: int) -> int:
        with self.con:
            return self.con.execute(
                "INSERT INTO salas (nome, capacidade) VALUES (?, ?)",
                (nome, capacidade)).lastrowid

    def salas(self) -> list[dict]:
        return [dict(l) for l in self.con.execute(
            "SELECT * FROM salas ORDER BY capacidade, nome")]

    def sala(self, sala_id: int) -> dict | None:
        l = self.con.execute("SELECT * FROM salas WHERE id = ?",
                             (sala_id,)).fetchone()
        return dict(l) if l else None

    def reservas_do_dia(self, sala_id: int, dia: date) -> list[dict]:
        return [dict(l) for l in self.con.execute(
            "SELECT * FROM reservas WHERE sala_id = ? AND date(inicio) = ? "
            "ORDER BY inicio", (sala_id, dia.isoformat()))]

    def ocupadas(self, inicio: datetime, fim: datetime) -> set[int]:
        """Salas com alguma reserva que se sobrepõe ao intervalo."""
        linhas = self.con.execute(
            "SELECT DISTINCT sala_id FROM reservas "
            "WHERE inicio < ? AND ? < fim",
            (fim.isoformat(), inicio.isoformat()))
        return {l[0] for l in linhas}

    def criar_reserva(self, sala_id: int, responsavel: str,
                      participantes: int, inicio: datetime,
                      fim: datetime) -> int:
        with self.con:
            return self.con.execute(
                "INSERT INTO reservas (sala_id, responsavel, participantes,"
                " inicio, fim) VALUES (?, ?, ?, ?, ?)",
                (sala_id, responsavel, participantes,
                 inicio.isoformat(), fim.isoformat())).lastrowid

    def apagar_reserva(self, reserva_id: int) -> bool:
        with self.con:
            return self.con.execute("DELETE FROM reservas WHERE id = ?",
                                    (reserva_id,)).rowcount == 1
