# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Classes

# antes
class CalculadoraIVA:
    def __init__(self, taxa):
        self.taxa = taxa
    def calcular(self, valor):
        return valor * (1 + self.taxa)

# depois
def com_iva(valor, taxa=0.23):
    return valor * (1 + taxa)

print(CalculadoraIVA(0.23).calcular(100) == com_iva(100))
