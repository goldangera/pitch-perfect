import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://golda:123@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # e-mail configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") 
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production config child class
    Args:
        Config: The parent config class with general config classes
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing config child class
    Args:
        Config: The parent config class with General config settings
    '''
    pass
class DevConfig(Config):
    '''
    Dev config child class
    Args:
        Config: The parent config class with general config settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
# class Config:
#     pass

# class ProdConfig(Config):
#     pass

# class TestConfig(Config):
#     pass

# class DevConfig(Config):
#     DEBUG = True

# config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

