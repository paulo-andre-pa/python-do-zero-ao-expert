import os
from flask import Flask

def criar_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-apenas-local"),
        BASE_DADOS=os.path.join(app.instance_path, "tarefas.db"),
    )
    if config:
        app.config.update(config)
    os.makedirs(app.instance_path, exist_ok=True)

    from app import bd, auth, tarefas
    bd.registar(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(tarefas.bp)
    return app
