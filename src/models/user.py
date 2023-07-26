#version 1.1

#Importacion de Librerias
from src.database import db, ma
from src.enums import TypeDocument
from src.models.garment import Garment
from src.models.outfit import Outfit
from datetime import date,datetime
from werkzeug.security import generate_password_hash, check_password_hash

#Creación de Modelos
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(128),nullable=False)
    email = db.Column(db.String(60),unique=True,nullable=False)
    date_birth = db.Column(db.Date,nullable=False)
    type_document = db.Column(db.Enum(TypeDocument),nullable=False,default=TypeDocument.cedula)
    garments = db.relationship('Garment', backref="owner")
    outfits = db.relationship('Outfit', backref="owner")
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    def __init__(self, **fields):
        super().__init__(**fields)
    
    def __repr__(self) -> str:
        return f"User >>> {self.name}"
    
    def __setattr__(self, name, value):
        if(name == "password"):
            value = User.hash_password(value)
        super(User, self).__setattr__(name, value)
    
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields
        model = User
        include_fk = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)