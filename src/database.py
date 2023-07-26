#Versión 1.1

#Importación de librerias
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

#Instanciar Objetos
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
