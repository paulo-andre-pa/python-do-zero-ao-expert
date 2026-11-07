# Capítulo 14 — Programação funcional e decoradores
# Secção: Closures

def criar_multiplicador(fator):
    def multiplicar(x):
        return x * fator          # 'fator' vem do âmbito envolvente
    return multiplicar

dobro = criar_multiplicador(2)
iva = criar_multiplicador(1.23)
print(dobro(21), round(iva(100), 2))
