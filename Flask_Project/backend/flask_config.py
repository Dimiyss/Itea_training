class Config():
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'SuperSecret#Key'
    FLASK_SECRET = SECRET_KEY


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
