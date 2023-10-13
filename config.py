import os
basedir = os.path.abspath(os.path.dirname(__file__))    # Returns the banking-project directory and directory of specified files
                                                        # making its content available to the flask app
from decouple import config
class Config:           
    SECRET_KEY = config('SECRET_KEY', default= os.environ.get('SECRET_KEY'))
    
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, os.environ.get('DEV_DATABASE_URL'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, os.environ.get('TEST_DATABASE_URL'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, os.environ.get('DATABASE_URL'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}