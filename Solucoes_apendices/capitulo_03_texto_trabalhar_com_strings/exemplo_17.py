# Capítulo 3 — Texto: trabalhar com strings
# Secção: Unicode e codificação

PARTICULAS = {"da", "de", "do", "dos", "das", "e"}

def normalizar(nome):
    palavras = nome.split()
    resultado = []
    for i, p in enumerate(palavras):
        p = p.lower()
        if i > 0 and p in PARTICULAS:
            resultado.append(p)
        else:
            resultado.append(p.capitalize())
    return " ".join(resultado)

print(normalizar("  mARIA   da  SILVA   "))
print(normalizar("JOÃO DOS SANTOS e COSTA"))
