# Capítulo 9 — Ficheiros e exceções
# Secção: Exceções: quando algo corre mal

def dividir(a, b):
    try:
        resultado = float(a) / float(b)
    except ValueError:
        return "Erro: valores não numéricos"
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    else:
        return f"{resultado:.2f}"        # só se não houve erro
    finally:
        print(f"[dividir({a!r}, {b!r}) terminou]")   # sempre

print(dividir("10", "4"))
print(dividir("10", "0"))
print(dividir("dez", "2"))
