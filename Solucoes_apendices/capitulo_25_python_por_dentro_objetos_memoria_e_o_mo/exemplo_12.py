# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: O caminho de uma operação
# Este exemplo termina, de propósito, com uma exceção.

class Ponto:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, outro):
        return (self.x, self.y) == (outro.x, outro.y)

{Ponto(1, 2)}
