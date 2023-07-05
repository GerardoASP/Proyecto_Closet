#Version 1.0
from flask import Flask
from os import environ
from src.endpoints.users import users
from src.endpoints.outfits import outfits
from src.endpoints.garments import garments
from src.endpoints.outfits_garments import outfits_garments

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config['ENVIRONMENT'] = environ.get("ENVIRONMENT")
    config_class = 'config.DevelopmentConfig'
    
    match app.config['ENVIRONMENT']:
        case "development":
            config_class = 'config.DevelopmentConfig'
        case "production":
            config_class = 'config.ProductionConfig'
        case _:
            print(f"ERROR: environment unknown: {app.config.get('ENVIRONMENT')},fallback to {mode}")
    
    app.config['ENVIRONMENT'] = "development"
    app.config.from_object(config_class)
    ##Load the blueprints
    app.register_blueprint(users)
    app.register_blueprint(outfits)
    app.register_blueprint(garments)
    app.register_blueprint(outfits_garments)
    return app