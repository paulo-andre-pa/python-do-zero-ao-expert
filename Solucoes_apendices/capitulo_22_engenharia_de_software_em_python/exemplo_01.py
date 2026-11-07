# Capítulo 22 — Engenharia de software em Python
# Secção: Logging

import logging, sys

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(name)s: %(message)s",
    stream=sys.stdout,
    force=True,
)
log = logging.getLogger("faturacao")

log.debug("detalhe técnico (não aparece: nível INFO)")
log.info("fatura FT 2026/118 emitida")
log.warning("cliente 4521 sem NIF; fatura emitida como consumidor final")
log.error("falha ao enviar a fatura por e-mail")
try:
    1 / 0
except ZeroDivisionError:
    log.exception("erro inesperado no cálculo do IVA")
