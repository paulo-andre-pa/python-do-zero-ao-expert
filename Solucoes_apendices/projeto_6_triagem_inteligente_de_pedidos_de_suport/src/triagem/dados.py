"""Gerador de pedidos de suporte sintéticos (para desenvolvimento)."""
import random

FRASES = {
    "faturacao": ["a fatura deste mês veio com um valor muito alto",
                  "fui cobrado duas vezes pelo mesmo serviço",
                  "quero pedir a segunda via da fatura",
                  "o débito direto falhou e agora tenho juros",
                  "não reconheço este valor no extrato",
                  "pedi o reembolso e ainda não recebi"],
    "tecnico": ["a internet está sempre a cair à noite",
                "o router tem a luz vermelha a piscar",
                "não tenho sinal de televisão desde ontem",
                "a velocidade da fibra está muito abaixo do contratado",
                "o telefone fixo não dá sinal de linha",
                "a box reinicia sozinha várias vezes"],
    "entregas": ["o equipamento ainda não chegou e já passou uma semana",
                 "o estafeta não apareceu na hora marcada",
                 "a encomenda do router veio danificada",
                 "quero alterar a morada de entrega",
                 "recebi o equipamento errado",
                 "o técnico de instalação não compareceu"],
    "conta": ["quero alterar a palavra-passe da área de cliente",
              "preciso de mudar o titular do contrato",
              "como atualizo o meu e-mail de contacto",
              "quero mudar para um tarifário mais barato",
              "não consigo entrar na área de cliente",
              "quero saber quando termina o período de fidelização"],
}
ABERTURAS = ["", "bom dia, ", "olá, ", "boa tarde. ", "exmos senhores, "]
FECHOS = ["", " obrigado", " aguardo resposta", " cumprimentos",
          " isto é inaceitável", " por favor ajudem"]
EXTRAS = ["", " já liguei duas vezes", " sou cliente há 10 anos",
          " o número de cliente é 123456", " desde segunda-feira"]

def _ruido(texto: str, rng: random.Random) -> str:
    if rng.random() < 0.15 and len(texto) > 10:       # erro de digitação
        i = rng.randrange(len(texto) - 1)
        texto = texto[:i] + texto[i + 1] + texto[i] + texto[i + 2:]
    return texto.upper() if rng.random() < 0.05 else texto

def gerar(n: int = 2000, semente: int = 7) -> tuple[list[str], list[str]]:
    rng = random.Random(semente)
    textos, rotulos = [], []
    categorias = list(FRASES)
    for _ in range(n):
        cat = rng.choice(categorias)
        frase = rng.choice(FRASES[cat])
        if rng.random() < 0.15:                       # pedidos ambíguos
            outra = rng.choice([c for c in categorias if c != cat])
            frase += " e também " + rng.choice(FRASES[outra])
        texto = rng.choice(ABERTURAS) + frase + rng.choice(EXTRAS) \
            + rng.choice(FECHOS)
        if rng.random() < 0.03:       # erros da triagem humana original
            cat = rng.choice(categorias)
        textos.append(_ruido(texto, rng))
        rotulos.append(cat)
    return textos, rotulos
