# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Dataclasses

from dataclasses import dataclass, asdict, replace

@dataclass(frozen=True, order=True)
class Versao:
    maior: int
    menor: int
    correcao: int = 0

    def __str__(self):
        return f"{self.maior}.{self.menor}.{self.correcao}"

versoes = [Versao(3, 12), Versao(3, 9, 7), Versao(2, 7, 18)]
print(max(versoes), sorted(versoes)[0])
v = Versao(3, 13)
print(replace(v, correcao=1), asdict(v))
print(hash(v) == hash(Versao(3, 13)))    # imutável: pode ser chave
