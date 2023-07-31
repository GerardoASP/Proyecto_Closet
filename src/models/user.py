#version 1.4

#Importacion de Librerias
from src.database import db, ma
from src.enums import TypeDocument
from src.models.garment import Garment
from src.models.outfit import Outfit
from datetime import date,datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates
import re

#Creación de Modelos
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(128),nullable=False) #Cambiar la cantidad de caracteres de la contraseña
    email = db.Column(db.String(60),unique=True,nullable=False)
    date_birth = db.Column(db.Date,nullable=False)
    type_document = db.Column(db.String(3),nullable=False)
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
    
    @staticmethod
    def hash_password(password):
        if not password:
            raise AssertionError('Password not provided')
        if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
            raise AssertionError('Password must contain 1 capital letter and 1 number')
        if len(password) < 7 or len(password) > 20:
            raise AssertionError('Password must be between 7 and 20 characters')
        
        return generate_password_hash(password)
    
    #Sección de Validación
    
    @validates('id')
    def validate_id(self, key, value):
        if not value:
            raise AssertionError('No id provided')
        if not re.compile("^[-+]?[0-9]+$", value):
            raise AssertionError('The value must be an integer')
        if value <= 0:
            raise AssertionError('id invalid')
        if User.query.filter(User.id == value).first():
            raise AssertionError('Id is already in use') 
        
        return value
    
    @validates('name')
    def validate_name_user(self,key,value):
        if not value:
            raise AssertionError('No name provided')
        if not value.isalnum():
            raise AssertionError('Name value must be alphanumeric')
        if len(value) < 5 or len(value) > 50:
            raise AssertionError('Name user must be between 5 and 50 characters')

        return value 
    
    @validates('email')
    def validate_email(self,key,value):
        if not value:
            raise AssertionError('No email provided')
        if not re.match("[^@]+@[^@]+\.[^@]+", value):
            raise AssertionError('Provided email is not an email address')
        if User.query.filter(User.email == value).first():
            raise AssertionError('Email is already in use')    
        return value
    
    @validates(date_birth)
    def validate_date_birth(self,key,value):
        # This field is not mandatory!
        if not value:
            raise value
        if not re.match("[0-9]{1,2}\\-[0-9]{1,2}\\-[0-9]{4}", value):
            raise AssertionError('Provided date is not a real date value')
        today = datetime.datetime.now()
        date_birth = datetime.datetime.strptime(value, "%Y-%m-%d")
        if not date_birth < today:
            raise AssertionError('date birth invalid')
        return value
    
    @validates('type_document')
    def validate_rol_user(self, key, value):
        allowed_values = [enum_value.value for enum_value in TypeDocument]
        if value not in allowed_values:
            raise ValueError('El valor del campo "type_document" no es válido. Los valores permitidos son c.c, t.i y c.e')
        return value

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields
        model = User
        include_fk = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)