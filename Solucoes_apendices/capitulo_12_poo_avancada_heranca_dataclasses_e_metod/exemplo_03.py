# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Polimorfismo

class Ficheiro:
    def ler(self):
        return "dados do disco"

class RespostaWeb:
    def ler(self):
        return "dados da rede"

def processar(fonte):          # aceita qualquer objeto com .ler()
    return fonte.ler().upper()

print(processar(Ficheiro()), "|", processar(RespostaWeb()))
