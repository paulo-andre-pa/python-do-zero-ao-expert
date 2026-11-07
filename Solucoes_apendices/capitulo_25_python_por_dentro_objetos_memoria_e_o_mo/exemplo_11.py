# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: O caminho de uma operação

class Exemplo:
    tipo = "atributo de classe"

    @property
    def valor(self):
        return "vem da property"

    def metodo(self):
        return "método"

e = Exemplo()
e.__dict__["valor"] = "no dicionário da instância"
e.__dict__["tipo"] = "no dicionário da instância"
print(e.valor)      # a property (descritor de dados) ganha
print(e.tipo)       # o dicionário da instância ganha ao atributo de classe
print(e.metodo)     # funções são descritores: produzem um método ligado
print(Exemplo.__dict__["metodo"])
