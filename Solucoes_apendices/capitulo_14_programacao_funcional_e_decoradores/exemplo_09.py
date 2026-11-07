# Capítulo 14 — Programação funcional e decoradores
# Secção: Decoradores

def anunciar(func):
    def envolvente(*args, **kwargs):
        print(f"-> a chamar {func.__name__}{args}")
        resultado = func(*args, **kwargs)
        print(f"<- {func.__name__} devolveu {resultado!r}")
        return resultado
    return envolvente

@anunciar                  # equivale a: somar = anunciar(somar)
def somar(a, b):
    return a + b

somar(2, 3)
