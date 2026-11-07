# Capítulo 14 — Programação funcional e decoradores
# Secção: Decoradores

import functools

def requer_perfil(*perfis):
    def decorador(func):
        @functools.wraps(func)
        def envolvente(utilizador, *args, **kwargs):
            if utilizador.get("perfil") not in perfis:
                nome = utilizador["nome"]
                raise PermissionError(f"{nome} não pode: {func.__name__}")
            return func(utilizador, *args, **kwargs)
        return envolvente
    return decorador

@requer_perfil("admin", "gestor")
def apagar_cliente(utilizador, id_cliente):
    return f"cliente {id_cliente} apagado por {utilizador['nome']}"

print(apagar_cliente({"nome": "Eva", "perfil": "admin"}, 42))
try:
    apagar_cliente({"nome": "Rui", "perfil": "estagiario"}, 42)
except PermissionError as e:
    print("Negado:", e)
