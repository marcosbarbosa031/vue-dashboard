class Config(object):
    ################ Common Config ###################

    TESTING = False


class DevConfig(Config):
    ################ Development Config ###################

    FLASK_DEBUG = True
    SQLALCHEMY_ECHO = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    ################ Production Config ###################

    FLASK_DEBUG = False


app_config = {
    'development': DevConfig,
    'production': ProdConfig
}
