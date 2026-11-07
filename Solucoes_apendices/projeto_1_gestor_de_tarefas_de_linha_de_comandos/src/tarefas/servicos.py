"""Regras de negócio do gestor de tarefas."""
from collections import Counter
from collections.abc import Callable
from datetime import date, timedelta

from tarefas.modelos import Prioridade, Tarefa
from tarefas.repositorio import RepositorioTarefas

class TarefaInexistente(LookupError):
    def __init__(self, id_: int) -> None:
        super().__init__(f"não existe a tarefa n.º {id_}")

class GestorTarefas:
    def __init__(self, repo: RepositorioTarefas,
                 hoje: Callable[[], date] = date.today) -> None:
        self.repo = repo
        self.hoje = hoje

    def interpretar_prazo(self, texto: str | None) -> date | None:
        if not texto:
            return None
        t = texto.strip().lower()
        if t == "hoje":
            return self.hoje()
        if t in ("amanha", "amanhã"):
            return self.hoje() + timedelta(days=1)
        if t.startswith("+") and t[1:].isdigit():
            return self.hoje() + timedelta(days=int(t[1:]))
        try:
            return date.fromisoformat(t)
        except ValueError:
            raise ValueError(f"prazo inválido: '{texto}' (use AAAA-MM-DD, "
                             "hoje, amanha ou +N)") from None

    def adicionar(self, titulo: str, prioridade: str = "media",
                  prazo: str | None = None, etiquetas: str = "") -> Tarefa:
        tarefa = Tarefa(titulo, Prioridade.de_texto(prioridade),
                        self.interpretar_prazo(prazo), etiquetas.split(","))
        return self.repo.guardar(tarefa)

    def _obter(self, id_: int) -> Tarefa:
        tarefa = self.repo.obter(id_)
        if tarefa is None:
            raise TarefaInexistente(id_)
        return tarefa

    def concluir(self, id_: int) -> Tarefa:
        tarefa = self._obter(id_)
        tarefa.concluida = True
        return self.repo.guardar(tarefa)

    def remover(self, id_: int) -> None:
        if not self.repo.apagar(id_):
            raise TarefaInexistente(id_)

    def listar(self, incluir_concluidas: bool = False,
               etiqueta: str | None = None) -> list[Tarefa]:
        return [t for t in self.repo.todas()
                if (incluir_concluidas or not t.concluida)
                and (etiqueta is None or etiqueta.lower() in t.etiquetas)]

    def estatisticas(self) -> dict[str, int]:
        todas = self.repo.todas()
        pendentes = [t for t in todas if not t.concluida]
        hoje = self.hoje()
        por_prioridade = Counter(t.prioridade.name.lower()
                                 for t in pendentes)
        return {"total": len(todas), "pendentes": len(pendentes),
                "concluidas": len(todas) - len(pendentes),
                "atrasadas": sum(t.atrasada(hoje) for t in pendentes),
                **{f"prioridade_{p}": n for p, n in por_prioridade.items()}}
