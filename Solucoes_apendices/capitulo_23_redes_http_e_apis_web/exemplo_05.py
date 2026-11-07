# Capítulo 23 — Redes, HTTP e APIs web
# Secção: Segurança e boas práticas

import hashlib, secrets, hmac

def gerar_hash(palavra_passe: str) -> str:
    sal = secrets.token_bytes(16)
    h = hashlib.scrypt(palavra_passe.encode(), salt=sal, n=2**14, r=8, p=1)
    return sal.hex() + ":" + h.hex()

def verificar(palavra_passe: str, guardado: str) -> bool:
    sal_hex, h_hex = guardado.split(":")
    h = hashlib.scrypt(palavra_passe.encode(), salt=bytes.fromhex(sal_hex),
                       n=2**14, r=8, p=1)
    return hmac.compare_digest(h.hex(), h_hex)   # comparação segura

registo = gerar_hash("Segura#2026")
print(len(registo), verificar("Segura#2026", registo),
      verificar("segura#2026", registo))
