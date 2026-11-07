# Capítulo 23 — Redes, HTTP e APIs web
# Secção: FastAPI: a framework moderna
# Exemplo ilustrativo: pode exigir pacotes ou serviços externos.

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="API de Tarefas", version="1.0")

class NovaTarefa(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)

class Tarefa(NovaTarefa):
    id: int
    feita: bool = False

tarefas: dict[int, Tarefa] = {}

@app.get("/tarefas")
def listar() -> list[Tarefa]:
    return list(tarefas.values())

@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar(nova: NovaTarefa) -> Tarefa:
    tarefa = Tarefa(id=len(tarefas) + 1, **nova.model_dump())
    tarefas[tarefa.id] = tarefa
    return tarefa

@app.delete("/tarefas/{tid}", status_code=status.HTTP_204_NO_CONTENT)
def apagar(tid: int) -> None:
    if tarefas.pop(tid, None) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "não encontrada")
