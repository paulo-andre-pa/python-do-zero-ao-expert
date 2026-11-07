# Capítulo 22 — Engenharia de software em Python
# Secção: Logging

import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=5,
                              encoding="utf-8")
handler.setFormatter(logging.Formatter(
    "%(asctime)s %(levelname)s [%(name)s] %(message)s"))
app_log = logging.getLogger("app")
app_log.setLevel(logging.INFO)
app_log.addHandler(handler)
app_log.propagate = False

app_log.info("arranque da aplicação, versão %s", "2.4.1")
print(open("app.log", encoding="utf-8").read().split(" ", 2)[2].strip())
