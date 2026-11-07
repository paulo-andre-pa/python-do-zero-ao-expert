# Capítulo 13 — Iteradores, geradores e compreensões
# Secção: O módulo itertools

import random
from collections import deque
from itertools import islice

def sensor():
    minuto = 0
    while True:
        yield minuto, random.gauss(22, 3)
        minuto += 1

def media_movel(leituras, janela=5):
    ultimas = deque(maxlen=janela)
    for minuto, valor in leituras:
        ultimas.append(valor)
        if len(ultimas) == janela:
            yield minuto, sum(ultimas) / janela

def alertas(medias, limite=25):
    for minuto, media in medias:
        if media > limite:
            yield f"min {minuto:>3}: média {media:.1f} °C acima de {limite}"

for a in islice(alertas(media_movel(sensor())), 3):
    print(a)
