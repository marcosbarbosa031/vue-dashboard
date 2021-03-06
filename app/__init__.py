# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager


# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
# login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True,
                static_folder="../dist/static", template_folder="../dist")
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    # login_manager.init_app(app)
    # login_manager.login_message = "You must be logged in to access this page"

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .card import card as card_blueprint
    app.register_blueprint(card_blueprint)

    from .boleto import boleto as boleto_blueprint
    app.register_blueprint(boleto_blueprint)

    from .deposit import deposit as deposit_blueprint
    app.register_blueprint(deposit_blueprint)

    from .transfer import transfer as transfer_blueprint
    app.register_blueprint(transfer_blueprint)

    from .auth import auth as auth_bluprint
    app.register_blueprint(auth_bluprint)

    from .company import company as company_bluprint
    app.register_blueprint(company_bluprint)

    return app
