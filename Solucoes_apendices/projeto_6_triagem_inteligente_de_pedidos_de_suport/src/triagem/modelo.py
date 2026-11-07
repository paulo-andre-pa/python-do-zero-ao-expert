"""Treino, avaliação e persistência do classificador."""
import unicodedata
from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# Palavras de cortesia e ligação que não indicam nenhuma categoria.
PALAVRAS_VAZIAS = """a o as os e de da do das dos em no na um uma que se
por para com ja ha isto ola bom dia boa tarde noite exmos senhores obrigado
obrigada cumprimentos favor ajuda ajudem preciso aguardo resposta tambem
sou cliente inaceitavel""".split()

def normalizar(texto: str) -> str:
    """Minúsculas e sem acentos: 'Fatura' e 'fátura' ficam iguais."""
    decomposto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in decomposto
                   if unicodedata.category(c) != "Mn")

def criar_pipeline() -> Pipeline:
    tfidf = TfidfVectorizer(preprocessor=normalizar, ngram_range=(1, 2),
                            stop_words=PALAVRAS_VAZIAS, min_df=2,
                            sublinear_tf=True)
    return Pipeline([("tfidf", tfidf),
                     ("clf", LogisticRegression(max_iter=2000, C=5.0))])

def treinar(textos: list[str], rotulos: list[str], semente: int = 0):
    X_tr, X_te, y_tr, y_te = train_test_split(
        textos, rotulos, test_size=0.2, random_state=semente,
        stratify=rotulos)
    modelo = criar_pipeline().fit(X_tr, y_tr)
    relatorio = classification_report(y_te, modelo.predict(X_te), digits=3)
    return modelo, (X_te, y_te), relatorio

def guardar(modelo, caminho: Path) -> None:
    joblib.dump(modelo, caminho)

def carregar(caminho: Path):
    return joblib.load(caminho)

def palavras_chave(modelo, n: int = 5) -> dict[str, list[str]]:
    """As n palavras com mais peso para cada categoria (explicabilidade)."""
    vocab = modelo["tfidf"].get_feature_names_out()
    clf = modelo["clf"]
    return {cat: [vocab[i] for i in clf.coef_[k].argsort()[::-1][:n]]
            for k, cat in enumerate(clf.classes_)}
