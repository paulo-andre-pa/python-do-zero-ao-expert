# Capítulo 18 — Tipagem estática e mypy
# Secção: Anotações básicas

nome: str = "Ana"
idade: int = 30
precos: list[float] = [9.99, 4.5]
stock: dict[str, int] = {"parafuso": 120}
coordenada: tuple[float, float] = (38.72, -9.14)
registo: tuple[int, ...] = (1, 2, 3, 4)       # tamanho variável

def saudacao(nome: str, vezes: int = 1) -> str:
    return ("Olá, " + nome + "! ") * vezes

def registar(mensagem: str) -> None:           # não devolve nada
    print(mensagem)

registar(saudacao("Rui", 2))
print(saudacao.__annotations__)
