#Version 1.1
from os import environ
class Config:
    """Base config"""
    FLASK_APP = environ.get('FLASK_APP')
    ENVIRONMENT = environ.get('ENVIRONMENT')
class DevelopmentConfig(Config):
    """Development config"""
    SECRET_KEY = environ.get('DEVELOPMENT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DEVELOPMENT_DATABASE_URI')
    TESTING = True
class ProductionConfig(Config):
    """Production config"""
    SECRET_KEY = environ.get('PRODUCTION_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('PRODUCTION_DATABASE_URI')
    TESTING = False