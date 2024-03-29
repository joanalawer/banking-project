import os
basedir = os.path.abspath(os.path.dirname(__file__))    # Returns the banking-project directory and directory of specified files
                                                        # making its content available to the flask app
class Config:           
    SECRET_KEY = os.environ.get('SECRET_KEY', default= os.environ.get('SECRET_KEY'))
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[PeriBank]'
    FLASKY_MAIL_SENDER = 'PeriBank Admin <jlawer90@gmail.com>'
    FLASKY_ADMIN = os.environ.get('PERIBANK_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev_db.sqlite3')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
  
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_db.sqlite3')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prod_db.sqlite3')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}