# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Personalizar a criação de classes

def norma(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5

Ponto = type("Ponto", (), {"x": 0, "y": 0, "norma": norma})
p = Ponto(); p.x, p.y = 3, 4
print(type(Ponto), p.norma())
