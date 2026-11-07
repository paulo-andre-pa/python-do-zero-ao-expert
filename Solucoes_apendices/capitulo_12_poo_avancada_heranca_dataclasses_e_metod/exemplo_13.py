# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Herança ou composição?

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Veiculo(ABC):
    matricula: str
    marca: str
    preco_base: float

    @abstractmethod
    def preco_dia(self, fim_de_semana: bool) -> float: ...

    def custo(self, dias_uteis: int, dias_fds: int) -> float:
        return (dias_uteis * self.preco_dia(False)
                + dias_fds * self.preco_dia(True))

@dataclass
class Automovel(Veiculo):
    eletrico: bool = False
    def preco_dia(self, fim_de_semana):
        return self.preco_base + (10 if self.eletrico else 0)

@dataclass
class Carrinha(Veiculo):
    carga_kg: int = 1000
    def preco_dia(self, fim_de_semana):
        return self.preco_base + 0.15 * self.carga_kg

@dataclass
class Mota(Veiculo):
    def preco_dia(self, fim_de_semana):
        return self.preco_base * (0.8 if fim_de_semana else 1)

frota = [Automovel("AA-11-BB", "Renault", 35, eletrico=True),
         Carrinha("CC-22-DD", "Ford", 50, carga_kg=1200),
         Mota("EE-33-FF", "Honda", 25)]
for v in sorted(frota, key=lambda v: v.custo(3, 2)):
    print(f"{type(v).__name__:<10}{v.matricula}  {v.custo(3, 2):>8.2f} €")
