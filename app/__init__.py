# Este es el punto de inicio de la aplicación
# es el módulo de la aplicación en si

from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializamos la conexión a la BD y agregamos la clase
    # para Login
    db.init_app(app)
    login_manager.init_app(app)

    # En esta sección agregamos los módulos creados para
    # redireccionar las rutas conforme se utiliza la aplicación
    
    from app.main.routes import main
    from app.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app