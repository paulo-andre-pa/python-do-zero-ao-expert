"""Aplicação do regulamento da biblioteca."""
from collections import Counter
from datetime import date

from biblioteca.dominio import Emprestimo, Livro, Socio, TipoSocio
from biblioteca.erros import (EmprestimoDuplicado, LimiteAtingido,
                              LivroIndisponivel, NaoEncontrado,
                              SocioImpedido)

LIMITE_MULTAS = 5.00

class Biblioteca:
    def __init__(self) -> None:
        self.livros: dict[str, Livro] = {}
        self.socios: dict[int, Socio] = {}
        self.emprestimos: list[Emprestimo] = []

    # --- cadastro -------------------------------------------------------
    def adicionar_livro(self, livro: Livro) -> None:
        if livro.isbn in self.livros:
            self.livros[livro.isbn].exemplares += livro.exemplares
        else:
            self.livros[livro.isbn] = livro

    def inscrever(self, numero: int, nome: str,
                  tipo: TipoSocio = TipoSocio.ESTUDANTE) -> Socio:
        socio = Socio(numero, nome, tipo)
        self.socios[numero] = socio
        return socio

    def _livro(self, isbn: str) -> Livro:
        if isbn not in self.livros:
            raise NaoEncontrado(f"livro {isbn} não existe")
        return self.livros[isbn]

    def _socio(self, numero: int) -> Socio:
        if numero not in self.socios:
            raise NaoEncontrado(f"sócio {numero} não existe")
        return self.socios[numero]

    # --- consultas ------------------------------------------------------
    def ativos(self, *, isbn: str | None = None,
               socio: int | None = None) -> list[Emprestimo]:
        return [e for e in self.emprestimos if e.ativo
                and (isbn is None or e.isbn == isbn)
                and (socio is None or e.socio == socio)]

    def disponiveis(self, isbn: str) -> int:
        return self._livro(isbn).exemplares - len(self.ativos(isbn=isbn))

    def pesquisar(self, termo: str) -> list[Livro]:
        t = termo.casefold()
        return sorted((l for l in self.livros.values()
                       if t in l.titulo.casefold()
                       or t in l.autor.casefold()), key=lambda l: l.titulo)

    def atrasados(self, hoje: date) -> list[Emprestimo]:
        return sorted((e for e in self.ativos() if e.dias_atraso(hoje)),
                      key=lambda e: e.prevista)

    def mais_requisitados(self, n: int = 3) -> list[tuple[str, int]]:
        contagem = Counter(e.isbn for e in self.emprestimos)
        return [(self.livros[i].titulo, c)
                for i, c in contagem.most_common(n)]

    # --- operações ------------------------------------------------------
    def emprestar(self, isbn: str, numero: int, hoje: date) -> Emprestimo:
        self._livro(isbn)
        socio = self._socio(numero)
        if socio.multas > LIMITE_MULTAS:
            raise SocioImpedido(
                f"{socio.nome} tem {socio.multas:.2f} € de multas")
        meus = self.ativos(socio=numero)
        if any(e.dias_atraso(hoje) for e in meus):
            raise SocioImpedido(f"{socio.nome} tem livros em atraso")
        if len(meus) >= socio.tipo.max_livros:
            raise LimiteAtingido(
                f"limite de {socio.tipo.max_livros} livros atingido")
        if any(e.isbn == isbn for e in meus):
            raise EmprestimoDuplicado("o sócio já tem este livro")
        if self.disponiveis(isbn) < 1:
            raise LivroIndisponivel("sem exemplares disponíveis")
        emprestimo = Emprestimo.novo(isbn, socio, hoje)
        self.emprestimos.append(emprestimo)
        return emprestimo

    def devolver(self, isbn: str, numero: int, hoje: date) -> float:
        for e in self.ativos(isbn=isbn, socio=numero):
            e.devolucao = hoje
            multa = e.multa(hoje)
            self.socios[numero].multas += multa
            return multa
        raise NaoEncontrado("não há empréstimo ativo deste livro ao sócio")

    def pagar(self, numero: int, valor: float) -> float:
        socio = self._socio(numero)
        socio.multas = round(max(0.0, socio.multas - valor), 2)
        return socio.multas
