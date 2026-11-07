# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Classes abstratas
# Este exemplo termina, de propósito, com uma exceção.

class Triangulo(Forma):
    def area(self):
        return 0.0

Triangulo()      # falta implementar perimetro()
