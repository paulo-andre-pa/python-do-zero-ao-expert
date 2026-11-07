from triagem import dados, modelo

def test_exatidao_minima_e_reprodutibilidade():
    textos, rotulos = dados.gerar(1500, semente=1)
    m, (X_te, y_te), _ = modelo.treinar(textos, rotulos)
    assert m.score(X_te, y_te) >= 0.9
    m2, _, _ = modelo.treinar(textos, rotulos)
    assert (m.predict(X_te) == m2.predict(X_te)).all()

def test_normalizar_remove_acentos_e_maiusculas():
    assert modelo.normalizar("Fatura NÃO Recebida") == "fatura nao recebida"

def test_guardar_e_carregar(tmp_path):
    m, (X_te, _), _ = modelo.treinar(*dados.gerar(600, semente=2))
    caminho = tmp_path / "m.joblib"
    modelo.guardar(m, caminho)
    assert list(modelo.carregar(caminho).predict(X_te[:20])) == \
        list(m.predict(X_te[:20]))
