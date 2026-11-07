# Capítulo 18 — Tipagem estática e mypy
# Secção: Validação em execução: pydantic

from pydantic import BaseModel, Field, ValidationError

class NovoUtilizador(BaseModel):
    nome: str = Field(min_length=2)
    idade: int = Field(ge=0, le=130)
    email: str
    newsletter: bool = False

u = NovoUtilizador(nome="Joana", idade="34", email="j@ex.pt")
print(u, type(u.idade))
try:
    NovoUtilizador(nome="J", idade=-3, email="x")
except ValidationError as e:
    print(e.error_count(), "erros:",
          [err["loc"][0] for err in e.errors()])
